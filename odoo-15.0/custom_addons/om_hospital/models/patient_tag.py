from odoo import api, models, fields

class PatientTag(models.Model):
    _name = 'patient.tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient Tag'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default='True')
    color = fields.Integer(string='Color')
    sequence = fields.Integer(string="Sequence", default = 0)

    _sql_constraints = [
        ('unique_tag_name', 'unique((name))', 'Tag Name must be unique'),
        ('check_sequence', 'check(sequence > 0)', 'Sequence must be Non ZERO positive number')

    ]