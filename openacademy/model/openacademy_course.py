from openerp import models, fields, api
 


class Course(models.Model):
    _name = 'openacademy.course'  # Model odoo name

    name = fields.Char(string='Title', required=True)  # Field reserved to identified name record
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', 
                                     string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session','course_id', string="Sessions")
    
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),
    
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
