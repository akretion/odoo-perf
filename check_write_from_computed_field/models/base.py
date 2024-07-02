# Copyright 2024 Akretion (https://www.akretion.com).
# @author Kévin Roche <kevin.roche@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class BaseModel(models.AbstractModel):
    _inherit = "base"

    @api.model
    def _compute_field_value(self, field):
        self = self.with_context(compute_field=field)
        return super(BaseModel, self)._compute_field_value(field)

    def write(self, vals):
        if self._context.get("compute_field") and self._name != "ir.attachment":
            _logger.warning(
                "Write operation triggered by computed field on model: "
                f"model :{self._name}, "
                f"field : {self._context.get('compute_field')}, "
                f"vals: {vals} "
                f"context: {self._context}, "
            )
        return super(BaseModel, self).write(vals)
