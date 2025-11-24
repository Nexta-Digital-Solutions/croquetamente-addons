# -*- coding: utf-8 -*-
# (c) 2023 Nexta - Jaume Basiero <jbasiero@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a

from odoo import models, fields, _



class StockPicking(models.Model):
    _inherit = 'stock.picking'

    valued_picking = fields.Boolean(string='Albarán Valorado', related="partner_id.valued_picking", readonly=False)

