# Copyright 2025 Akretion (https://www.akretion.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    commercial_partner_id = fields.Many2one(index=True)
    partner_id = fields.Many2one(index=True)
    partner_shipping_id = fields.Many2one(index=True)
