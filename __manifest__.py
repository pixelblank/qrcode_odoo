# -*- coding: utf-8 -*-
{
    'name': 'QrCode Generateur deluxe',
    'version': '1.0',
    'summary': 'Ce module sert à générer des QrCode trop beau',
    'author': "Pixelblank",
    'sequence': 10,
    'description': 'Ce module sert à générer des QrCode',
    'category': 'Uncategorized',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/qrcode_module.xml',
        'views/qrcode_menu.xml',
        'views/qrcode_action.xml',
        'views/qrcode_list_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}