# Copyright 2025 Akretion (https://www.akretion.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def init(self):
        res = super().init()
        # the _compute_quantities_dict in stock/models/product.py
        # do a complex read_group
        # add a specific index to improve perf (in a real customer case less 3s on
        # so validation)
        self.env.cr.execute(
            """
            CREATE INDEX IF NOT EXISTS stock_move_read_group
            ON stock_move
            (state, product_id, location_id, location_dest_id, date, company_id)
            """
        )
        return res
