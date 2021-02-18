# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    negative_move_id = fields.Many2one(index=True)
