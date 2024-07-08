from odoo import models, fields

class Subject(models.Model):
    _name = 'subject.subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    lecturer_id = fields.Many2one('res.partner', string='Lecturer', domain=[('is_lecturer', '=', True)])