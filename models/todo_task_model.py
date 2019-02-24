from odoo import api, fields, models

class TodoTask(models.Model):
    _inherit = 'todo.task'
    effort_estimate = fields.Integer()
    name = fields.Char(help="What needs to be done?")

    # Relational fields
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')

    # Dynamic reference fields
    refers_to = fields.Reference(
        [('res.user', 'User'), ('res.partner', 'Partner')],
        'Refers to')

    # Computed fields
    stage_fold = fields.Boolean(
        'Stage Folded?',
        compute='_compute_stage_fold')

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for todo in self:
            todo.stage_fold = todo.stage_id.fold
