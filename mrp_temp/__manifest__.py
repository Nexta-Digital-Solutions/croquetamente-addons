# -*- coding: utf-8 -*-
{
    'name': "Mrp temperature",
    'summary': """Añade campo de temperatura en las ordenes de trabajo""",
    'description': """Añade campo de temperatura en las ordenes de trabajo""",
    'author': "NextaDS",
    'website': "https://www.nextads.es",
    'category': 'CRM',
    'version': '18.0.0.1',
    'license': "LGPL-3",
    'depends': [
        'mrp_workorder',
    ],

    'data': [
        'views/mrp_workcenter_view.xml',
        'views/mrp_workorder_views.xml',
    ],

    'installable': True
}