from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer Of Project'

    name = fields.Char(String='Name')

    @api.constrains('name')
    def check_name(self):
        for item in self:
            subject = self.env['customer'].search([('name', '=', item.name), ('id', '!=', item.id)])
            if subject:
                raise ValidationError(_("Name " + item.name + " Already Exists"))

    # One2Many field
    models_ids = fields.One2many('project.study', 'customer_id', string='Customer')
