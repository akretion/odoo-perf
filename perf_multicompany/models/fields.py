# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.fields import Field

ori_setup_attrs = Field._setup_attrs

# Run me as server_wide module and then run an update all


def _setup_attrs(self, model, name):
    ori_setup_attrs(self, model, name)
    # Always index the fields company_id
    if name == "company_id":
        self.index = True


Field._setup_attrs = _setup_attrs
