# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('supplier_search'):
            args.append(['supplier', '=', True])
        return super(ResPartner, self).name_search(
            name, args=args, operator=operator, limit=limit)
