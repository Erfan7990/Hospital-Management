from datetime import date, datetime
from odoo import api, models, fields


class PatientAccount(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient Information'

    name = fields.Char(string='Name', tracking=True)
    reference = fields.Char(string='Reference')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='age', tracking=True, compute='_compute_age')
    gender = fields.Selection([('male', "Male"), ('female', 'Female')])
    patient_problem = fields.Char(string='Patient Problem')
    active = fields.Boolean(string='Active', default='True')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for res in self:
            today = date.today()
            if res.date_of_birth:
                res.age = today.year - res.date_of_birth.year
            else:
                res.age = 0
