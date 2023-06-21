import datetime
from odoo import api, fields, models

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    # ----76. Default get function----
    @api.model
    def default_get(self, fields_list):
        res = super(CancelAppointmentWizard, self).default_get(fields_list)
        res['cancel_date'] = datetime.date.today()
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    reason = fields.Text(string="Reason")
    cancel_date = fields.Date(string='Cancellation Date')


    def action_cancel(self):
        return