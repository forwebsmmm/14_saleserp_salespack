# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY touch:n:track <https://tnt.pythonanywhere.com>
# Part of SalesERP Partner Birthday addon for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SalesERP Partner Birthday',
    'version': '0.1',
    'summary': '''Add Birthday Field in Partner''',
    'description': '''Add Birthday Field in Partner''',
    'category': 'Extra Tools',
    'author': 'SalesERP',
    'website': 'https://tnt.pythonanywhere.com',
    'depends': ['contacts'],
    'data': [
        'views/partner_form_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
