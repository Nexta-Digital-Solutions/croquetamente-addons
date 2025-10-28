# -*- coding: utf-8 -*-
from odoo import api, Command, fields, models

class ProjectProject(models.Model):
    _inherit = "project.project"

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsable del proyecto',
        help="Person in charge of the project.",
    )


class PorjectTask(models.Model):
    _inherit = "project.task"

    employee_ids = fields.Many2many(
        comodel_name="hr.employee",
        string="Asignados",
        help="People assigned to the task.",
    )
