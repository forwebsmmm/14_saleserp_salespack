# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY SalesERP <https://saleserp.pro/>
# Part of SalesERP KOATUU Cities addon for Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

city_categories = ('C', 'С', 'М', 'Щ', 'Т')
country_capital_code = '8000000000'
state_capital_ls_code = '10100000'


class ResCity(models.Model):
    _inherit = 'res.city'

    koatuu_city = fields.Many2one('saleserp.cities.hierarchy', string='KOATUU City', readonly=True)

    @api.model
    def update_cities(self):
        koatuu_cities = self.sudo().search([('koatuu_city', '!=', None)])
        koatuu_cities_ids = [c.koatuu_city.id for c in koatuu_cities]
        cities = self.env['saleserp.cities.hierarchy'].sudo().search([
            '|', '|',
            ('category', 'in', city_categories),
            ('code', '=', country_capital_code),
            '&', '&', '&', '&', '&',
            ('state_code', '!=', ''),
            ('second_lvl', '!=', ''),
            ('third_lvl', '=', ''),
            ('fourth_lvl', '=', ''),
            ('category', '=', ''),
            ('second_lvl_ls', '=', state_capital_ls_code),
        ])
        for city in cities:
            district_id = self.env['saleserp.cities.hierarchy'].sudo().search([('code', '=', city.state_code)]).id
            state_id = self.env['res.country.state'].sudo().search([('koatuu_state', '=', district_id)]).id
            if city.id in koatuu_cities_ids:
                rec = self.sudo().search([('koatuu_city', '=', city.id)])
                rec.write({
                    'name': city.name,
                    'district_id': state_id,
                })
            else:
                self.create({
                    'koatuu_city': city.id,
                    'name': city.name,
                    'district_id': state_id,
                })
