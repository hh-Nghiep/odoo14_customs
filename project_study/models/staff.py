from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Staff(models.Model):
    _name = 'staff'
    _description = 'Task For Staff'

    name = fields.Char(String='Name')

    # One2Many field
    models_ids = fields.One2many('project.study', 'staff_id', String='Staff')
    task2_ids = fields.One2many('task2', 'assign_to', String='Staff')

    @api.constrains('name')
    def check_name(self):
        for item in self:
            subject = self.env['staff'].search([('name', '=', item.name), ('id', '!=', item.id)])
            if subject:
                raise ValidationError(_("Name " + item.name + " Already Exists"))
