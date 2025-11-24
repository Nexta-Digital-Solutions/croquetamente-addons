# -*- coding: utf-8 -*-
# (c) 2023 Nexta - Jaume Basiero <jbasiero@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a
from itertools import product

from odoo import models, fields, _, api



class StockQuant(models.Model):
    _inherit = 'stock.quant'

    package_qty = fields.Float(string="Package Qty",  required=False,compute="compute_package_qty" )

    @api.depends('product_id', 'product_uom_id', 'quantity')
    def compute_package_qty(self):
        for quant in self:
            package_qty = 0
            if quant.product_id and quant.quantity and quant.product_uom_id and quant.product_id.packaging_ids:
                packaging_id = quant.product_id.packaging_ids
                package_qty = quant.quantity / packaging_id.qty
            quant.update({
                'package_qty': package_qty
            })

