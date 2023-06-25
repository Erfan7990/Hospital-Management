from datetime import date, datetime

from dateutil import relativedelta

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class PatientAccount(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient Information'
    _rec_name = 'reference'

    name = fields.Char(string='Name', tracking=True)
    reference = fields.Char(string='Reference')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='age', tracking=True, compute='_compute_age', inverse='_inverse_compute_age')
    gender = fields.Selection([('male', "Male"), ('female', 'Female')])
    patient_problem = fields.Char(string='Patient Problem')
    active = fields.Boolean(string='Active', default='True')
    appointment_id = fields.One2many('hospital.appointment', 'patient_id', string='Appointment')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count', store=True)
    # appointment_doctor = fields.Char(string="Appointment Doctor",  compute="_compute_appointment_doctor", store=True)
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([
        ('married', 'Married'),
        ('single', 'Single'),
    ], string="Marital Status", tracking=True)
    partner_name = fields.Char(string='Partner Name')



    @api.depends('appointment_id')
    def _compute_appointment_count(self):
        for res in self:
            res.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', res.id)])

    # def _compute_appointment_doctor(self):
    #     for res in self:
    #         res.appointment_doctor = self.env['hospital.appointment'].search_name([('patient_id', '=', res.id)])



        # for i in self.appointment_id:
        #     self.appointment_doctor = i.doctor_id
        # self.appointment_id = self.appointment_id.doctor_id

    # ---- Constrains in odoo -------
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for res in self:
            if res.date_of_birth and res.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not Correct !"))

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

    # ----- use @api.ondelete operation-----------
    @api.ondelete(at_uninstall=False)
    def _check_appointment(self):
        for rec in self:
           if rec.appointment_id:
               raise ValidationError(_("You cannot delete patient Information"))

    # ----77. Name get function----
    def name_get(self):
        patient_list=[]
        for record in self:
            name = record.reference + '-' + record.name
            patient_list.append((record.id, name))
        return patient_list

    def action_test(self):
        print("Clicked...........")

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years = rec.age)
