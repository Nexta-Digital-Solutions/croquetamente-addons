# -*- coding: utf-8 -*-
{
    'name': "Sale Lines Stock Alert",
    'summary': """Añade una alerta para cuando en el producto quedan menos de la cantidad indicada""",
    'description': """Añade una alerta para cuando en el producto quedan menos de la cantidad indicada""",
    'author': "NextaDS",
    'website': "https://www.nextads.es",
    'category': 'Stock',
    'version': '18.0.0.2',
    'license': "LGPL-3",
    'depends': [
        'stock',
        'product',
        'sale',
    ],

    'data': [
        'views/product_template_views.xml'
    ],

    'installable': True
}