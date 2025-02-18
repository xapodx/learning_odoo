from odoo import fields,models


class ChangeState(models.TransientModel):
    _name = 'state'


    grade_id = fields.Many2one('grade', string='Grade')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
    ],default='draft')
    reason = fields.Char()

    def action_confirm(self):
        self.property_id=self.state