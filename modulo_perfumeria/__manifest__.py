{
    'name': "Modulo_perfumeria",
    'summary': "Modulo de la perfumeria",
    'description': "Introduccion a odoo",
    'author': "Anthony",
    'website': "",
    'category': "Tools",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/perfume_view.xml',
        'views/grupo_view.xml',
        'views/cliente_view.xml',
        'views/tienda_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
