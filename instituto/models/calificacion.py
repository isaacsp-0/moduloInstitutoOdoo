from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Calificacion(models.Model):
    _name = 'instituto.calificacion'
    _description = 'instituto.calificacion'

    name = fields.Float(string="Nota", required=True)
    estudiante = fields.Many2one("instituto.estudiante", string="Estudiante", required=True)
    asignatura = fields.Many2one("instituto.asignatura", string="Asignatura", required=True)

    @api.onchange('estudiante')
    def _onchange_estudiante(self):
        if self.estudiante:
            asignaturas_asignadas = self.estudiante.asignatura.ids
            calificaciones_existentes = self.estudiante.calificaciones.mapped('asignatura.id')
            asignaturas_no_calificadas = [a for a in asignaturas_asignadas if a not in calificaciones_existentes]
            return {
                'domain': {
                    'asignatura': [('id', 'in', asignaturas_no_calificadas)]
                }
            }
        else:
            return {
                'domain': {
                    'asignatura': []
                }
            }

    _sql_constraints = [
        ('unique_estudiante_asignatura', 
         'UNIQUE(estudiante, asignatura)', 
         'Un estudiante no puede tener más de una calificación para la misma asignatura.')
    ]

    @api.constrains('name')
    def _comprobar_nota_maxima(self):
        for record in self:
            if record.name > 10 or record.name < 0:
                raise ValidationError("La nota no puede ser superior a 10 o menor que 0.")
