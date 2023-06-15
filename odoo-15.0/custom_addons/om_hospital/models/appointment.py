from odoo import api, models, fields


class PatientAccount(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient Appointment Information'
    _rec_name = 'patient_id'


    patient_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Date")
    booking_date= fields.Date(string="Booking Date", default=fields.Datetime.now)
    reference = fields.Char(string='Reference')
    prescription = fields.Html(string='prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string="Priority")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.reference = self.patient_id.reference