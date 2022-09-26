from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Project(models.Model):
    _name = 'project'
    _description = 'Project For Task'

    name = fields.Char(String='Name')

    # tags = fields.Selection([('new feature ', 'New')], default='new')

    @api.constrains('name')
    def check_name(self):
        for item in self:
            subject = self.env['project'].search([('name', '=', item.name), ('id', '!=', item.id)])
            if subject:
                raise ValidationError(_("Name " + item.name + " Already Exists"))

    # One2Many field
    models_ids = fields.One2many('project.study', 'project_id', string='Project')
