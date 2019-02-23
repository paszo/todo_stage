from odoo import api, fields, models

class TodoTask(models.Model):
    _inherit = 'todo.task'
    effort_estimate = fields.Integer()
    name = fields.Char(help="What needs to be done?")
