from datetime import timedelta, date

from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_ref = fields.Char(string="Employee Reference", readonly=True, copy=False, default='New')
    salary = fields.Float()
    shift = fields.Boolean(string="Shift", default=False)
    grade_id = fields.Many2one('property')

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
    ], string="Visa Status", compute='_compute_visa_status', store=True)

    @api.model
    def create(self, vals):
        if vals.get('employee_ref', 'New') == 'New':
            vals['employee_ref'] = self.env['ir.sequence'].next_by_code('emplooye_seq') or 'New'
        return super(HrEmployee, self).create(vals)

    @api.depends('housing_allowance', 'transport_allowance', 'medical_allowance', 'salary', 'shift')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.housing_allowance + rec.medical_allowance + rec.transport_allowance + rec.salary
            if rec.shift:
                rec.total += 2500  # Add 300 if the shift is True

    @api.depends('visa_expire')
    def _compute_visa_status(self):
        today = date.today()
        for rec in self:
            if rec.visa_expire:
                if rec.visa_expire < today:
                    rec.visa_status = 'expired'
                elif rec.visa_expire <= today + timedelta(days=30):
                    rec.visa_status = 'soon'
                else:
                    rec.visa_status = 'valid'

    def check_visa_expiration_date(self):
        employees = self.search([('visa_expire', '!=', False)])
        today = fields.Date.today()

        for emp in employees:
            old_status = emp.visa_status

            if emp.visa_expire < today:
                emp.write({'visa_status': 'expired'})
            elif emp.visa_expire <= today + timedelta(days=30):
                emp.write({'visa_status': 'soon'})
            else:
                emp.write({'visa_status': 'valid'})

            if old_status != emp.visa_status:
                print(f"Updated {emp.name}'s visa status to {emp.visa_status}")
