from odoo import fields, models

class ChangeState(models.TransientModel):
    _name = 'state'

    grade_id = fields.Many2one('grade', string='Grade', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
    ], default='draft')
    reason = fields.Char()

    def action_confirm(self):
            self.grade_id.state = self.state
