from odoo import models , fields

class property(models.Model):

    _name = 'property'

    name = fields.Char()
    housing = fields.Float()
    transport = fields.Float()
    mediacl = fields.Float()
    shift = fields.Boolean()
    not_shift = fields.Boolean()
    bouns = fields.Float()


