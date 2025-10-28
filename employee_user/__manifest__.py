# -*- coding: utf-8 -*-
{
    'name': "Employee Users",
    'summary': """
        Sustituye a los usuarios, para usar el empleado en:
        - Proyectos
        - Tareas
        - Ordenes de fabricación
        """,
    'description': """
        Sustituye a los usuarios, para usar el empleado en:
        - Proyectos
        - Tareas
        - Ordenes de fabricación
    """,
    'author': "NextaDS",
    'website': "https://nextads.es/",
    'category': 'Employee',
    'version': '18.0.0.1',
    "license": "AGPL-3",
    'depends': [
        'project',
        'mrp',
    ],

    'data': [
        'views/project_task.xml',
        'views/mrp_production.xml',
    ],
}
