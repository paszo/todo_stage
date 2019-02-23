from odoo import fields, models

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence, name'

    name = fields.Char('Name', translate=True)
    sequence = fields.Integer('Sequence')
