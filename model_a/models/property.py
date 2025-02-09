from odoo import models , fields

class property(models.Model):

    _name = 'property'

    name = fields.Char()
    housing = fields.Float()
    transport = fields.Float()
    mediacl = fields.Float()
    bouns = fields.Float()


