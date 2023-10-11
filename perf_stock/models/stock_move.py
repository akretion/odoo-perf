# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    product_qty = fields.Float(index=True)

    def init(self):
        super().init()
        # the _compute_quantities_dict in stock/models/product.py
        # do a complexe read_group
        # add a specific index to improve perf (in a real customer case less 3s on
        # so validation)
        self.env.cr.execute(
            """
            CREATE INDEX IF NOT EXISTS stock_move_read_group
            ON stock_move
            (state, product_id, location_id, location_dest_id, date, company_id)
            """
        )
