# -*- coding: utf-8 -*-
from odoo import api, Command, fields, models

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    employee_id = fields.Many2one('hr.employee', string='Responsable')

