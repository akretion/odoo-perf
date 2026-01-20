# Copyright 2024 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    categ_id = fields.Many2one(index="btree_not_null")
    product_id = fields.Many2one(index="btree_not_null")
    product_tmpl_id = fields.Many2one(index="btree_not_null")
    date_start = fields.Datetime(index="btree_not_null")
    date_end = fields.Datetime(index="btree_not_null")
