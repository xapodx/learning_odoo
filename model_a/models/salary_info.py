from odoo import models, fields

class Salary(models.Model):
    _name = 'salary'
    _description = 'Salary'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=True)
    grade_id = fields.Many2one('grade', required=True)
    shift = fields.Boolean(default=False)
    employee_id = fields.Many2one('hr.employee', string="Employee")

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Name must be unique!'),
    ]
