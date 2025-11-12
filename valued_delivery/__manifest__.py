# -*- coding: utf-8 -*-
{
    'name': "Albarán Valorado Check",
    'summary': """Añade un check para elegir si el impreso del albarán debe ser valorado""",
    'description': """Añade un check para elegir si el impreso del albarán debe ser valorado""",
    'author': "NextaDS",
    'website': "https://www.nextads.es",
    'category': 'Stock',
    'version': '18.0.0.1',
    'license': "LGPL-3",
    'depends': [
        'stock',
        'contacts',
        'stock_picking_report_valued',
    ],

    'data': [
        'views/valued_check_print.xml',
    ],

    'installable': True
}