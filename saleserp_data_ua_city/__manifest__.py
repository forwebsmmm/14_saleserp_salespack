# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY SalesERP <https://saleserp.pro/>
# Part of SalesERP KOATUU Cities addon for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SalesERP KOATUU Cities',

    'summary': '''
Cities from KOATUU
    ''',

    'description': '''
Import Cities from KOATUU
    ''',

    'author': 'SalesERP',
    'website': 'https://saleserp.pro/',
    'category': 'SalesERP',
    'version': '0.1',

    'depends': [
        'saleserp_data_ua_state',
        'partner_district',
    ],

    'data': [
        'views/backend_assets.xml',
    ],

    'qweb': [
        'static/src/xml/update_cities_button.xml',
    ],

    'installable': True,
    'auto_install': False,
}
