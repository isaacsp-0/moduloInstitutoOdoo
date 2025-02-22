from odoo import models, fields, api
from odoo.exceptions import ValidationError

class grupo(models.Model):
    _name = 'instituto.grupo'
    _descripcion = 'instituto.grupo'

    name = fields.Char(string="Grupo", required=True)

    tutor = fields.Many2one("instituto.profesor", string="Tutor")

    anio = fields.Integer(string="Año", required=True)

    estudiantes = fields.Many2many("instituto.estudiante", string="Estudiantes")

    curso = fields.Many2one("instituto.curso", string="Curso")


    @api.constrains('name')
    def comprobarDato(self):
        for record in self:
            if (record.name and len(record.name) > 1 ):
                    raise ValidationError("¡El grupo no puede contener más de una letra como identificador!")

    @api.constrains('estudiantes', 'anio')
    def _check_estudiante_unico_por_anio(self):
        for record in self:
            for estudiante in record.estudiantes:
                grupos_con_mismo_estudiante = self.env['instituto.grupo'].search([
                    ('id', '!=', record.id),  
                    ('anio', '=', record.anio),  
                    ('estudiantes', 'in', estudiante.id)  
                ])
                if grupos_con_mismo_estudiante:
                    raise ValidationError(f"El estudiante {estudiante.name} ya está en otro grupo en el año {record.anio}.")
                
    def name_get(self):
        result = []
        for grupo in self:
            name = f"{grupo.curso.name if grupo.curso else 'Sin curso'} - {grupo.name}"
            result.append((grupo.id, name))
        return result