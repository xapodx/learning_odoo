from datetime import timedelta, date

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_ref = fields.Char(string="Employee Reference", readonly=True, copy=False, default='New')
    salary = fields.Float()
    shift = fields.Boolean(string="Shift", default=False)
    grade_id = fields.Many2one('grade')

    # Using the related field to link allowances to the 'grade_id'
    medical_allowance = fields.Float(related='grade_id.mediacl', string="Medical")
    transport_allowance = fields.Float(related='grade_id.transport', string="Transport")
    housing_allowance = fields.Float(related='grade_id.housing', string="Housing")
    bouns_allowance = fields.Integer(related='grade_id.bouns', string="Bouns")
    total = fields.Float(compute='_compute_total', store=True, readonly=1)
    visa_expire = fields.Date(string="Visa Expiry Date")
    visa_status = fields.Selection([
        ('valid', " Valid"),
        ('soon', " Expiring Soon"),
        ('expired', " Expired")
    ], string="Visa Status", store=True)

    # Field for storing the visa status color
    visa_status_color = fields.Char(string=".", store=1)

    # Creating the sequence
    @api.model
    def create(self, vals):
        if vals.get('employee_ref', 'New') == 'New':
            vals['employee_ref'] = self.env['ir.sequence'].next_by_code('employee_seq') or 'New'
        return super(HrEmployee, self).create(vals)

    # Computing the total salary
    @api.depends('housing_allowance', 'transport_allowance', 'medical_allowance', 'salary', 'shift')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.housing_allowance + rec.medical_allowance + rec.transport_allowance + rec.salary
            if rec.shift:
                rec.total += 2500  # Add 2500 if the shift is True



    # Function to check and update the visa expiration date status
    def check_visa_expiration_date(self):
        employees = self.search([('visa_expire', '!=', False)])
        today = fields.Date.today()

        for emp in employees:

            # Check the visa expiration date and update the status
            if emp.visa_expire < today:
                emp.write({'visa_status': 'expired', 'visa_status_color': 'red'})
            elif emp.visa_expire <= today + timedelta(days=30):
                emp.write({'visa_status': 'soon', 'visa_status_color': 'orange'})
            else:
                emp.write({'visa_status': 'valid', 'visa_status_color': 'green'})

