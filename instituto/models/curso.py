from odoo import models, fields, api
from odoo.exceptions import ValidationError

class curso(models.Model):
    _name = 'instituto.curso'
    _description = 'Curso'
    
    name = fields.Integer(string="Número del curso", required=True)
    grupos = fields.Many2many("instituto.grupo", string="Grupos", domain="[('curso', '=', id)]") 

    @api.constrains('grupos')
    def _check_grupos_curso(self):
        for record in self:
            for grupo in record.grupos:
                if grupo.curso.id != record.id:
                    raise ValidationError(f"El grupo {grupo.name} pertenece a un curso diferente ({grupo.curso.name}).")