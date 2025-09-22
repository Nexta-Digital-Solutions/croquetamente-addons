# -*- coding: utf-8 -*-
# (c) 2025 Nexta - Carlos Ros <cros@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a

from odoo import models, api, _, fields
from odoo.exceptions import UserError

class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    need_temp = fields.Boolean(string="Refrigerado?")

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    temperature = fields.Float(string="Temperatura refrigerado")

    def action_mark_as_done(self):
        if self.workcenter_id.need_temp and (not self.temperature or self.temperature == 0):
            raise UserError(_("No se ha establecido la temperatura"))
        return super().action_mark_as_done()

