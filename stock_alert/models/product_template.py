# -*- coding: utf-8 -*-
# (c) 2025 Nexta - Carlos Ros <cros@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a
from odoo import models, fields, _, api



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    alert = fields.Boolean(string="Alert",  )
    qty_to_alert = fields.Integer(string="Quantity to alert")

