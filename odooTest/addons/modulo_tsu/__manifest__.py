# -*- coding: utf-8 -*-
{
    'name': "Academia",

    'summary': "Gestión de cursos académicos",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
         'views/curso_views.xml'
    ],
    # only loaded in demonstration mode
    'application': True,
    'installable': True,
}

