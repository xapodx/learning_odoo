from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrGrade(models.Model):
    _name = 'hr.grade'
    _description = 'Employee Grade'
    _inherit = ['mail.thread']

    name = fields.Char(string="Grade Name", required=True, help="e.g., 'Grade A', 'Grade B'")
    allowance_housing = fields.Float(string="Housing Allowance", default=250.0)
    allowance_transport = fields.Float(string="Transport Allowance")
    allowance_medical = fields.Float(string="Medical Allowance")
    allowance_food = fields.Float(string="Food Allowance")
    bonus_percentage = fields.Float(string="Bonus Percentage")
    allowance_shift = fields.Boolean(string="Shift Allowance", default=False)
    
    # Computed field for total allowances
    total_allowances = fields.Float(
        string="Total Allowances", 
        compute='_compute_total_allowances',
        store=True,
        readonly=True
    )
    
    # State field for approval workflow
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ], string="State", default='draft')

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Grade name must be unique!'),
        ('positive_bonus', 'CHECK(bonus_percentage >= 0)', 'Bonus percentage must be positive!'),
    ]

    @api.depends('allowance_housing', 'allowance_transport', 'allowance_medical', 'allowance_food')
    def _compute_total_allowances(self):
        for rec in self:
            rec.total_allowances = (
                rec.allowance_housing + 
                rec.allowance_transport + 
                rec.allowance_medical + 
                rec.allowance_food
            )

    @api.constrains('bonus_percentage')
    def _check_bonus_percentage(self):
        for rec in self:
            if rec.bonus_percentage < 0 or rec.bonus_percentage > 100:
                raise ValidationError('Bonus percentage must be between 0 and 100!')

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'

    def action_approved(self):
        for rec in self:
            rec.state = 'approved'