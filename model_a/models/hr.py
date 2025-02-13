from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    salary = fields.Float()
    shift = fields.Boolean(string="Shift", default=False)
    grade_id = fields.Many2one('property')

    # Using the related field to link allowances to the 'grade_id'
    medical_allowance = fields.Float(related='grade_id.mediacl', string="Medical")
    transport_allowance = fields.Float(related='grade_id.transport', string="Transport")
    housing_allowance = fields.Float(related='grade_id.housing', string="Housing")
    bouns_allowance = fields.Integer(related='grade_id.bouns', string="Bouns")
    total = fields.Float(compute='_compute_total', store=True, readonly=1)

    @api.depends('housing_allowance', 'transport_allowance', 'medical_allowance', 'salary', 'shift')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.housing_allowance + rec.medical_allowance + rec.transport_allowance + rec.salary
            if rec.shift:
                rec.total += 300  # Add 300 if the shift is True
