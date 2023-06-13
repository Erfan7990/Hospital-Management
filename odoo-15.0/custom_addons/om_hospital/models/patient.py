from odoo import api, models, fields


class PatientAccount(models.Model):
    _name = 'hospital.patient'
    _discription = 'Hospital Patient Informatiom'

    name = fields.Char(string='Name')
    age = fields.Integer(string='age')
    gender = fields.Selection([('male', "Male"), ('female', 'Female')])
    patient_problem = fields.Char(string='Patient Problem')
