from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Task2(models.Model):
    _name = 'task2'
    _description = 'Model For Task2'

    name = fields.Char(String='Name', required=True)
    dateline = fields.Date(String='DateLine', required=True)
    note = fields.Text(String='Note')
    description = fields.Text(String='Description')
    status = fields.Selection([('to_do', "To Do"), ('in_progress', "In Progress"), ('review', "Review"),
                               ('done', "Done")], default='to_do', String='Status', required=True)

    # One2Many field
    assign_to = fields.Many2one('staff', String='Assign To', required=True)

    # @api.constrains('name')
    # def check_name(self):
    #     for item in self:
    #         subject = self.env['staff'].search([('name', '=', item.name), ('id', '!=', item.id)])
    #         if subject:
    #             raise ValidationError(_("Name " + item.name + " Already Exists"))
