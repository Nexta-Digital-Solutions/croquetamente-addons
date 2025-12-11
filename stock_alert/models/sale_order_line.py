# -*- coding: utf-8 -*-
# (c) 2025 Nexta - Carlos Ros <cros@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a
from odoo import models, fields, _, api



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    @api.depends('product_id')
    def show_stock_quantity_alert(self):
        for line in self:
            if line.product_id.qty_available > line.product_id.qty_to_alert:
                message = _("There is less than the amount indicated in the alert for product {}.").format(line.product_id.display_name)
                return {'warning': {'title': _('Warning'), 'message': message}}

