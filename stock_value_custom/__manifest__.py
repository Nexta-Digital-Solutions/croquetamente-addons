# -*- coding: utf-8 -*-
{
    'name': "Stock Location Report",
    'summary': """Este módulo permite añade cantidad embalaje para saber cuanto espacio ocupado hay de cada producto""",
    'description': """Este módulo permite añade cantidad embalaje para saber cuanto espacio ocupado hay de cada producto""",
    'author': "NextaDS",
    'website': "https://www.nextads.es",
    'category': 'Stock',
    'version': '18.0.0.2',
    'license': "LGPL-3",
    'depends': [
        'stock',
        'product',
    ],

    'data': [
        'views/stock_quant_views.xml',
    ],

    'installable': True
}