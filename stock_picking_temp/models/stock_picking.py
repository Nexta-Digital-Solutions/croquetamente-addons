# -*- coding: utf-8 -*-
# (c) 2025 Nexta - Carlos Ros <cros@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a

from odoo import models, api, _, fields
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = 'stock.move'

    temperature = fields.Float(string="Temperatura refrigerado")

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        for line in self.move_ids_without_package:
            if line.picking_id.picking_type_id.code == 'incoming' and (not line.temperature or line.temperature == 0):
                raise UserError(_("No se ha establecido la temperatura"))
            picking = super().button_validate()
        return picking