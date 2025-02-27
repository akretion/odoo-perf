# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    sale_id = fields.Many2one(index=True)
    owner_id = fields.Many2one(index=True)
    partner_id = fields.Many2one(index=True)
