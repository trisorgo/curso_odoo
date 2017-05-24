# -*- coding: utf-8 -*-
{
    'name': "Open Academy Session",

    'summary': """Manage trainings""",

    'description': """
        Open Academy Session module for checking sessions:
            - Restricción cuando un alumno se apunta a una sesión si tiene otra
            confirmada en las mismas fechas. Opción de apuntarse en reserva de plazas
    """,

    'author': "Trini Sorlí",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','openacademy'],

    # always loaded
    'data': [
            'views/openacademy.xml',
            ],
    # only loaded in demonstration mode
    'demo': [
            ],
    'installable': True,
    'active': False,
}
