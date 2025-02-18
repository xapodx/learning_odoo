
from odoo import models , fields, api



class jobs(models.Model):

    _name = 'jobs'
    _description = 'jobs'
    _inherit = ['mail.thread']


    name = fields.Char(string="name",required=1)
    grade_id=fields.Many2one('grade', required=True)
    shift=fields.Boolean(default=False)

    _sql_constraints = [
        ('unique_name', 'UNIQUE("name")', 'Name must be unique!'),

    ]
