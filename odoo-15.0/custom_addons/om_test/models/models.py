# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_Order(models.Model):
    _inherit = 'sale.order'

    confirmed_user = fields.Many2one('res.users', string='Confirmed User')

    def action_confirm(self):
        super(sale_Order, self).action_confirm()
        print("Success.................")
        self.confirmed_user = self.env.user.id




