# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY SalesERP <https://saleserp.pro/>
# Part of SalesERP Lost Reasons addon for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SalesERP Lost Reasons',

    'summary': '''
Lost Reasons for CRM
    ''',

    'description': '''
Add Lost Reasons to crm.lost.reason model
    ''',

    'author': 'SalesERP',
    'website': 'https://saleserp.pro/',
    'category': 'SalesERP',
    'version': '0.1',

    'depends': [
        'crm',
    ],

    'data': [
        'data/saleserp_lost_reason_data.xml',
    ],

    'installable': True,
    'auto_install': False,
}
