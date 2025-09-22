# -*- coding: utf-8 -*-
{
    'name': "Stock picking temperature",
    'summary': """Añade campo de temperatura""",
    'description': """Añade campo de temperatura""",
    'author': "NextaDS",
    'website': "https://www.nextads.es",
    'category': 'CRM',
    'version': '18.0.0.1',
    'license': "LGPL-3",
    'depends': [
        'stock',
    ],

    'data': [
        'views/stock_picking_views.xml',
    ],

    'installable': True
}