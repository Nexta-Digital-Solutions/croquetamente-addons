# -*- coding: utf-8 -*-
# (c) 2025 Nexta - Carlos Ros <cros@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a

from odoo import models, api, _, fields
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    temperature = fields.Float(string="Temperatura")

    def button_validate(self):
        if self.picking_type_code == 'incoming' and (not self.temperature or self.temperature == 0):
            raise UserError(_("No se ha establecido la temperatura"))
        picking = super().button_validate()
        return picking