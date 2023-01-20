# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models

CHECK_MODELS = [
    "sale.order.line",
    "stock.inventory.line",
    "purchase.order.line",
]


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _filter_not_deletable(self):
        if not self:
            return self
        self.flush()
        not_deletable_ids = set()
        for model_name in CHECK_MODELS:
            if model_name in self.env:
                table = self.env[model_name]._table
                self.env.cr.execute(
                    f"""SELECT product_id
                    FROM {table}
                    WHERE product_id in %s
                    GROUP BY product_id
                    """,
                    (tuple(self.ids),),
                )
                ids = [x[0] for x in self.env.cr.fetchall()]
                not_deletable_ids |= set(ids)
        return self.browse(not_deletable_ids)

    def _unlink_or_archive(self, check_access=True):
        # native unlink is super slow
        # First get not deletable product (and flag them like in product_variant_inactive)
        # Then call super to try to unlink them but do it one by one
        # as most of the time dichotomy is super slow for this work

        # like in product_variant_inactive skip record flagged as deleted
        records = self.filtered(lambda s: not s.combination_deleted)

        if records:
            # then quickly get not deletable product
            not_deletable = records._filter_not_deletable()
            not_deletable.write({"combination_deleted": True, "active": False})
            deletable = records - not_deletable
            for record in deletable:
                super(ProductProduct, record)._unlink_or_archive(
                    check_access=check_access
                )
        return True
