from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'
    
    name = fields.Char(string = "DNI", required = True)
    
    nombre = fields.Char(string = "Nombre", required = True)
    
    apellido = fields.Char(string = "Apellido", required = True)
    
    fechaNac = fields.Date(string = "Fecha de nacimiento", required = True)
    
    direccion = fields.Char(string = "Dirección", required = True)
    
    telefono = fields.Char(string = "Teléfono", required = True)
    
    fotoProfesor = fields.Char(string="Image URL")
    
    foto = fields.Boolean(string="Is Image URL Set", compute="_compute_foto")
      
    especialidad = fields.Char(string = "Especialidad", required = True)


    _sql_constraints = [
        ('dni_unique', 'unique(name)', 'El DNI debe ser único.'),
    ]

    @api.depends('fotoProfesor')
    def _compute_foto(self):
        for record in self:
            record.foto = True if record.fotoProfesor else False

    @api.constrains('name')
    def _check_dni(self):
        for record in self:
            dni = record.name
            if not dni or len(dni) != 9:
                raise ValidationError('El DNI debe tener 8 números y 1 letra.')

            numero = dni[:-1]
            letra = dni[-1].upper()
            letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"

            if not numero.isdigit():
                raise ValidationError('Los primeros 8 caracteres del DNI deben ser números.')

            if letra != letras_validas[int(numero) % 23]:
                raise ValidationError('La letra del DNI no es válida.')

    @api.constrains('telefono')
    def _check_telefono(self):
        for record in self:
            if record.telefono and not record.telefono.isdigit():
                raise ValidationError('El teléfono solo debe contener números.')
            if record.telefono and len(record.telefono) < 9:
                raise ValidationError('El teléfono debe tener al menos 9 dígitos.')

    @api.constrains('fechaNac')
    def _check_fechaNac(self):
        for record in self:
            if record.fechaNac and record.fechaNac > date.today():
                raise ValidationError('La fecha de nacimiento no puede ser posterior a la actual.')
    