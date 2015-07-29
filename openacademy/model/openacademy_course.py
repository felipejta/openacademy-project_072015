from openerp import models, fields, api
 


class Course(models.Model):
    _name = 'openacademy.course'  # Model odoo name

    name = fields.Char(string='Title', required=True)  # Field reserved to identified name record
    description = fields.Text(string='Description')
