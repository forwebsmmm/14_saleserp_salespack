# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY SalesERP <https://saleserp.pro/>
# Part of SalesERP KOATUU States addon for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SalesERP KOATUU States',

    'summary': '''
States from KOATUU
    ''',

    'description': '''
Import States from KOATUU
    ''',

    'author': 'SalesERP',
    'website': 'https://saleserp.pro/',
    'category': 'SalesERP',
    'version': '0.1',

    'depends': [
        'saleserp_data_ua_koatuu',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/backend_assets.xml',
        'views/success_wizard_view.xml'
    ],

    'qweb': [
        'static/src/xml/update_state_button.xml',
    ],

    'installable': True,
    'auto_install': False,
}
