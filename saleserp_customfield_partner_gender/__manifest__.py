# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY touch:n:track <https://tnt.pythonanywhere.com>
# Part of SalesERP Partner Gender addon for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SalesERP Partner Gender',
    'version': '0.1',
    'summary': '''Add Gender Field in Partner''',
    'description': '''Add Gender Field in Partner''',
    'category': 'Extra Tools',
    'author': 'SalesERP',
    'website': 'https://tnt.pythonanywhere.com',
    'depends': ['contacts'],
    'data': [
        'views/partner_form_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
