# Buat model subject_line dengan nama **subject.line** dengan list field sbb:
#     - subject_id - Many2one (subject.subject, required)
#     - lecturer_id - Many2one (res.partner, related=subject_id.lecturer_id)
#     - start_hour - float (widget float_time)
#     - end_hour - float (widget float_time)

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SubjectLine(models.Model):
    _name = 'subject.line'
    _description = 'Subject Line'

    subject_id = fields.Many2one('subject.subject', string='Subject', required=True)
    lecturer_id = fields.Many2one('res.partner', related='subject_id.lecturer_id', string='Lecturer')
    start_hour = fields.Float(string='Start Hour', widget='float_time')
    end_hour = fields.Float(string='End Hour', widget='float_time')
    class_id = fields.Many2one('class.class', string='Class')
    
    @api.onchange('start_hour')
    def _check_start_hour_format(self):
        for record in self:
            if record.start_hour:
                try:
                    hour, minute = divmod(record.start_hour * 60, 60)
                    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                        raise ValidationError("Invalid start hour format. Please use HH:MM format.")
                except Exception:
                    raise ValidationError("Invalid start hour format. Please use HH:MM format.")

    @api.onchange('end_hour')
    def _check_end_hour_format(self):
        for record in self:
            if record.end_hour:
                try:
                    hour, minute = divmod(record.end_hour * 60, 60)
                    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                        raise ValidationError("Invalid end hour format. Please use HH:MM format.")
                except Exception:
                    raise ValidationError("Invalid end hour format. Please use HH:MM format.")
                
    @api.onchange('start_hour', 'end_hour')
    def _check_start_end_hour(self):
        for record in self:
            if record.start_hour and record.end_hour:
                if record.start_hour >= record.end_hour:
                    raise ValidationError("Start hour must be less than end hour.")