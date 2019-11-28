# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    company_id = fields.Many2one(index=True)
    procurement_group_id = fields.Many2one(index=True)
    partner_id = fields.Many2one(auto_join=True)
