# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def write(self, vals):
        # when adding/removing attribute line
        # odoo is going to recompute variant ids after each action
        # and so it will create a lot of useless variant that will be removed after
        # so skip all variant creation and create them only at the end
        res = super(
            ProductTemplate, self.with_context(skip_create_variant_ids=True)
        ).write(vals)
        if (
            "attribute_line_ids" in vals
            or (vals.get("active") and len(self.product_variant_ids) == 0)
            # This adds support for the module product_attribute_variant_rules
            # Avoiding the need to create a glue module:
            or ("use_attribute_rules" in vals or "product_attribute_rule_ids" in vals)
        ):
            if vals.get("active"):
                self = self.with_context(skip_reactivate_variant=False)
            self._create_variant_ids()
        return res

    def _create_variant_ids(self):
        if self._context.get("skip_create_variant_ids"):
            return True
        else:
            return super()._create_variant_ids()
