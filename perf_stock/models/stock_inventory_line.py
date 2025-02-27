# Copyright 2025 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import fields, models


class StockInventoryLine(models.Model):
    _inherit = "stock.inventory.line"

    partner_id = fields.Many2one(index=True)
