from odoo import fields, models

class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'
    name = fields.Char('Name', translate=True)

    # Many2many inverse relationship
    task_ids = fields.Many2many('todo.task', string = 'Tasks')
