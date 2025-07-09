from odoo import models, fields, api
from odoo.exceptions import ValidationError


class property(models.Model):

    _name = 'property'
    _inherit = ['mail.thread']
    _description = 'Property'

    name = fields.Char(string="Name", required=1)
    housing = fields.Float(default=250)
    transport = fields.Float()
    medical = fields.Float()
    bonus = fields.Integer(required=1)
    total = fields.Float(compute='_compute_total', store=0, readonly=1)
    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('approved','Approved'),
    ],
        default='draft'
    )
    _sql_constraints = [
        ('unique_name', 'UNIQUE("name")', 'Name must be unique!'),
        ('unique_bonus', 'UNIQUE(bonus)', 'Bonus must be unique!')
    ]

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
        #self.write({'state':'draft'}) we can make it this way too

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'


    def action_approved(self):
                for rec in self:
                    rec.state = 'approved'


    @api.depends('housing', 'medical', 'transport')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.housing + rec.medical + rec.transport

    @api.constrains('bonus')
    def _check_bonus(self):
        for rec in self:
            if rec.bonus < 0:
                raise ValidationError('the bonus cant be less than 0')

    @api.model_create_multi
    def create(self,vals):
        res = super(property, self).create(vals)
        print("inside")
        return res

    @api.model #read fonk
    def _search(self,domain,offset=0,limit=None,order=None,access_rights_uid=None):
        res = super(property, self)._search(domain,offset=0,limit=None,order=None,access_rights_uid=None)
        print("inside, from search")
        return res


    def write(self,vals): #update fonk
        res=super(property,self).write(vals)
        print("inside, from write")
        return res

    def unlink(self): #delet fonk
        res=super(property,self).unlink()
        print("inside, unlink write")
        return res