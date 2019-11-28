# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _auto_init(self, cr, context=None):
        # group id is a related field with old API format
        # hack it without full field redefinition
        self._columns["group_id"].select = True
        return super(StockPicking, self)._auto_init(cr, context=context)
