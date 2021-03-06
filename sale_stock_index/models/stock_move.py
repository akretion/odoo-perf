# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    procurement_id = fields.Many2one(index=True)
    # Improve stock move unlink
    origin_returned_move_id = fields.Many2one(index=True)
    split_from = fields.Many2one(index=True)
