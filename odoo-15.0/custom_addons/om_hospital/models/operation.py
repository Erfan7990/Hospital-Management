from odoo import api, models, fields, _
from odoo.exceptions import ValidationError



class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"
    _log_access = False
    # _rec_name = 'doctor_id'

    doctor_id = fields.Many2one('res.users', string='Doctor')
    operation_name = fields.Char(string='Operation Name')
    reference_record = fields.Reference(selection=[('hospital.patient', 'Patient'),
                                                   ('hospital.appointment', 'Appointment')], string='Record')


    @api.model
    def name_create(self, name):
        return self.create({'operation_name': name}).name_get()[0]