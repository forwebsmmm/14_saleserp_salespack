# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY SalesERP <https://saleserp.pro/>
# Part of SalesERP Partner Categories addon for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SalesERP Partner Categories',

    'summary': '''
Partner Categories for Contacts
    ''',

    'description': '''
Add Partner Categories to res.partner.category model
    ''',

    'author': 'SalesERP',
    'website': 'https://saleserp.pro/',
    'category': 'SalesERP',
    'version': '0.1',

    'depends': [
        'base',
    ],

    'data': [
        'data/saleserp_partner_category_data.xml',
    ],


    'installable': True,
    'auto_install': False,
}
