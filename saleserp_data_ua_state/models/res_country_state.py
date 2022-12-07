# -*- coding: utf-8 -*-
# Copyright (C) 2016-TODAY SalesERP <https://saleserp.pro/>
# Part of SalesERP KOATUU States addon for Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleserpMessageWizard(models.TransientModel):
    _name = "saleserp.message.wizard"
    _description = "Message wizard to display warnings, alert ,success messages"

    def get_default(self):
        if self.env.context.get("message", False):
            return self.env.context.get("message")
        return False

    name = fields.Text(string="Message", readonly=True, default=get_default)


class ResCountryState(models.Model):
    _inherit = "res.country.state"

    koatuu_state = fields.Many2one("saleserp.cities.hierarchy", string="KOATUU State", readonly=True)

    @api.model
    def update_state(self):
        country_id = self.env['res.country'].sudo().search([('code', '=', 'UA')]).id
        koatuu_country_state = self.sudo().search([('koatuu_state', '!=', None), ('country_id', '=', country_id)])
        koatuu_country_state_ids = [s.koatuu_state.id for s in koatuu_country_state]
        states = self.env['saleserp.cities.hierarchy'].sudo().search([('parent_id', '=', None)])
        for state in states:
            if state.id in koatuu_country_state_ids:
                rec = self.sudo().search([('koatuu_state', '=', state.id)])
                rec.write({
                    'name': state.name,
                    'country_id': country_id,
                    'code': state.code[:2],
                })
            else:
                self.create({
                    'koatuu_state': state.id,
                    'name': state.name,
                    'country_id': country_id,
                    'code': state.code[:2],
                })
