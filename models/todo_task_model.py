from odoo import api, fields, models

class TodoTask(models.Model):
    _inherit = 'todo.task'
    effort_estimate = fields.Integer()
