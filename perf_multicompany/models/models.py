# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class Base(models.AbstractModel):
    _inherit = "base"

    def _modified_triggers(self, tree, create=False):
        for field, records, create in super()._modified_triggers(tree, create=False):
            if "company_id" in records._fields and len(records.company_id) > 1:

                if records._name in ["stock.warehouse.orderpoint"]:
                    _logger.debug("Perf: filter record only for current company")
                    records = records.filtered(
                        lambda s: s.company_id == self.env.company
                    )
                else:
                    _logger.warning(
                        "Performance danger detection. Notify recompute record from "
                        "different company model %s",
                        records._name,
                    )
            yield field, records, create
