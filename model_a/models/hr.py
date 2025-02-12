from odoo import models , fields



class Hr(models.Model):
    _inherit = 'hr.employee'

    property_id = fields.Many2one('property')


