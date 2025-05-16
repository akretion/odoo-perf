# Copyright 2022 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    template_specific_seller_ids = fields.One2many(
        "product.supplierinfo", "product_tmpl_id", domain=[("product_id", "=", False)]
    )
