from odoo import models , fields, api
from odoo.exceptions import ValidationError



class property(models.Model):

    _name = 'property'
    _inherit = ['mail.thread']
    _description = 'Property'

    name = fields.Char(required=1)
    housing = fields.Float(default=250)
    transport = fields.Float()
    mediacl = fields.Float()
    bouns = fields.Integer(required=1)


    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!')
    ]

    @api.constrains('bouns')
    def _check_bouns(self):
        for rec in self:
            if rec.bouns == 0:
                raise ValidationError('the bouns cant be less than 0')

    @api.model_create_multi
    def create(self,vals):
        res = super(property, self).create(vals)
        print("inside")
        return res


    