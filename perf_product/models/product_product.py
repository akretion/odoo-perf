# Copyright 2022 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.product.models import product


class ProductProduct(models.Model):
    _inherit = "product.product"

    variant_specific_seller_ids = fields.One2many("product.supplierinfo", "product_id")


# Monkey-patch native method to replace it without breaking inherit
def _prepare_sellers(self, params=False):
    return (
        self.variant_specific_seller_ids + self.template_specific_seller_ids
    ).sorted(lambda s: (s.sequence, -s.min_qty, s.price, s.id))


product.ProductProduct._prepare_sellers = _prepare_sellers
