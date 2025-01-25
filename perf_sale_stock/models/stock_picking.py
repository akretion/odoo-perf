# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    group_id = fields.Many2one(index=True)
    location_id = fields.Many2one(index=True)
    location_dest_id = fields.Many2one(index=True)
    picking_type_id = fields.Many2one(index=True)
    printed = fields.Boolean(index=True)
    immediate_transfer = fields.Boolean(index=True)
