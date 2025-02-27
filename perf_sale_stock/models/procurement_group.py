# Copyright 2025 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProcurementGroup(models.Model):
    _inherit = "procurement.group"

    sale_id = fields.Many2one(index=True)
