# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MailTrackingValue(models.Model):
    _inherit = "mail.tracking.value"

    field = fields.Many2one(index=True)
