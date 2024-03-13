# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    lot_producing_id = fields.Many2one(index=True)
    procurement_group_id = fields.Many2one(index=True)
    product_id = fields.Many2one(index=True)
