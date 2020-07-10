# -*- coding: utf-8 -*-
{
    'name': "Modulo de desarrollo",

    'summary': """
        """,

    'description': """
        Aprendizaje Odoo 12 / quadit
    """,

    'author': "Quadit",
    'website': "http://www.quadit.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'desarrollo',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/academy.xml', #Se agrega vista
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}