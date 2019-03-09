from odoo import api, fields, models
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']
    effort_estimate = fields.Integer()
    name = fields.Char(help="What needs to be done?")

    # Relational fields
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')

    # Dynamic reference fields
    refers_to = fields.Reference(
        [('res.user', 'User'), ('res.partner', 'Partner')],
        'Refers to')

    # Related fields
    state = fields.Selection(
        related='stage_id.state',
        string='Stage Stage')


    # Computed fields
    stage_fold = fields.Boolean(
        'Stage Folded?',
        compute='_compute_stage_fold',
        search='_search_stage_fold',
        inverse='_write_stage_fold')

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for todo in self:
            todo.stage_fold = todo.stage_id.fold

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        for todo in self:
            todo.stage_id.fold = todo.stage_fold

    # Chapter o4 SQL Constraints
    _sql_constraints = [(
        'todo_task_name_unique',
        'UNIQUE (name, active)',
        'Task title must be unique!'
    )]

    # Chapter 04 ORM (Python) Constraints
    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Title must have 5 chars!')

    @api.onchange('user_id')
    def onchange_user_id(self):
        if not self.user_id:
            self.team_ids = None
            return {
                'warning': {
                    'title': 'No Responsible',
                    'message': 'Team was also reset.'
                }
            }

    @api.model
    def create(self, vals):
        # Code before create: should use the 'vals' dict
        new_record = super().create(vals)
        # Code after create: can use the 'new record' created
        return new_record

    @api.multi
    def write(self, vals):
        # Code before write: can use 'self', with the old values
        super().write(vals)
        # Code after write: can use 'self', with the updated values
        return True
