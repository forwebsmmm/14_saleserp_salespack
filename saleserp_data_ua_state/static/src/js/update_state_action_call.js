odoo.define('saleserp_data_ua_state.update_state_action_button', function (require) {
"use strict";
var core = require('web.core');
var ListController = require('web.ListController');
var rpc = require('web.rpc');
var session = require('web.session');
var _t = core._t;
ListController.include({
   renderButtons: function($node) {
       this._super.apply(this, arguments);
           if (this.$buttons) {
             this.$buttons.find('.oe_update_state_action_button').click(this.proxy('action_def_state'));
           }
   },
   action_def_state: function () {
        var self = this
        return rpc.query({
            model: 'res.country.state',
            method: 'update_state',
        }).then(function (data) {
            self.do_action({
                name: 'Success',
                type: 'ir.actions.act_window',
                res_model: 'saleserp.message.wizard',
                view_mode: 'form',
                view_type: 'form',
                views: [[false, 'form']],
                target: 'new',
                context:{
                    message: 'States successfully imported!'
                }
            });
        });
   }
})
})