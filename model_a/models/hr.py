from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    property_id = fields.Many2one('property', string="Property")
    salary_id = fields.Many2one('salary', string="Salary")
    shift = fields.Boolean(string="Shift", default=False)
