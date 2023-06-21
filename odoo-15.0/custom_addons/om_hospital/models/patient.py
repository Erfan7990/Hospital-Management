from datetime import date, datetime
from odoo import api, models, fields


class PatientAccount(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient Information'
    _rec_name = 'reference'

    name = fields.Char(string='Name', tracking=True)
    reference = fields.Char(string='Reference')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='age', tracking=True, compute='_compute_age')
    gender = fields.Selection([('male', "Male"), ('female', 'Female')])
    patient_problem = fields.Char(string='Patient Problem')
    active = fields.Boolean(string='Active', default='True')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    appointment_doctor = fields.Char(string="Appointment Doctor")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string='Tags')

    # ------- Override Create method and generate the sequence of Patient -----------
    @api.model
    def create(self, vals_list):
        print('Reference............', vals_list)
        vals_list['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(PatientAccount, self).create(vals_list)


    # -------Override write the method-----------
    def write(self, vals):
        if not self.reference and not vals.get('ref'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(PatientAccount, self).write(vals)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for res in self:
            today = date.today()
            if res.date_of_birth:
                res.age = today.year - res.date_of_birth.year
            else:
                res.age = 0

    @api.onchange('appointment_id')
    def onchange_appointment_doctor(self):
        # for res in self:
        for i in self.appointment_id:
            self.appointment_doctor = i.doctor_id
        # self.appointment_id = self.appointment_id.doctor_id

    # ----77. Name get function----
    def name_get(self):
        patient_list=[]
        for record in self:
            name = record.reference + '-' + record.name
            patient_list.append((record.id, name))
        return patient_list