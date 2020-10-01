# -*- coding: utf-8 -*-
##############################################################################
#
#  licence AGPL version 3 or later
#  see licence in __openerp__.py or http://www.gnu.org/licenses/agpl-3.0.txt
#  Copyright (C) 2015 Akretion (http://www.akretion.com).
#
##############################################################################
from openerp import models, fields


class StockMoveOperationLink(models.Model):
    _inherit = "stock.move.operation.link"

    move_id = fields.Many2one('stock.move', 'Move', required=True,
        ondelete="cascade", index=True)
    operation_id = fields.Many2one('stock.pack.operation', 'Operation',
        required=True, ondelete="cascade", index=True)
