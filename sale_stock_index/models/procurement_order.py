# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"

    move_dest_id = fields.Many2one(index=True)
    production_id = fields.Many2one(index=True)
    sale_line_id = fields.Many2one(index=True)
    state = fields.Selection(index=True)
