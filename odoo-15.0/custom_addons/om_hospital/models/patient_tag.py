from odoo import api, models, fields

class PatientTag(models.Model):
    _name = 'patient.tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient Tag'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active')
    color = fields.Integer(string='Color')