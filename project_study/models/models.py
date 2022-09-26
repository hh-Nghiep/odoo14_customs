from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class EnmasysProjectStudy(models.Model):
    _name = 'project.study'
    _description = 'Enmasys Project Study'

    name = fields.Char(String='Name', size=20, trim=True, translate=True)
    start_date = fields.Date(String='Start Date', required=True)
    end_date = fields.Date(String='End Date', required=True)
    dateline = fields.Integer(String="Date Line")
    states = fields.Selection([('to_do', "To Do"), ('in_progress', "In Progress"), ('review', "Review"),
                               ('done', "Done")], default='to_do', String='States', required=True)

    # Many2Many Field
    customer_id = fields.Many2one('customer', String='Customer', required=True)
    staff_id = fields.Many2one('staff', String='Staff', required=True)
    project_id = fields.Many2one('project', String='Parent', required=True)

    # @api.onchange('assign_to')
    # def onchange_assign(self):
    #     date_today = fields.Datetime.now()
    #     date_object = datetime.strptime(str(date_today), '%Y-%m-%d %H:%M:%S')
    #     self.assignee_update_at = date_object

    @api.constrains('staff_id')
    def check_name(self):
        user_id = self.env['res.users'].browse(self._uid).id
        print(user_id)
        for item in self:
            subject = self.env['project.study'].search([('staff_id', '=', item.staff_id.id), ('id', '!=', item.id), '|',
                                                        ('start_date', '<=', item.start_date),
                                                        ('start_date', '<=', item.end_date), '|',
                                                        ('end_date', '>=', item.start_date),
                                                        ('end_date', '>=', item.end_date)])
            if (item.end_date - item.start_date).days == 0:
                self.dateline = 1
            else:
                self.dateline = (item.end_date - item.start_date).days
            if subject:
                raise ValidationError(_("This customer is existed at another task. Please choose another customer"))
