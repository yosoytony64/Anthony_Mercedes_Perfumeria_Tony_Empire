# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Modulo_perfumeria",
    'summary': "Modulo de la perfumeria",
    'description': "Introduccion a odoo",
    'author': "Anthony",
    'website': "",
    'category': "Tools",
    'version': '0.1',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
      'views/perfume_view.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
}
