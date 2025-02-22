from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import date


class estudiante(models.Model):
    _name = 'instituto.estudiante'
    _description = 'instituto.estudiante'

    name = fields.Char(string="Dni", required=True)

    nombre = fields.Char(string="Nombre", required = True)
    
    apellido = fields.Char(string="Apellido", required = True)
    
    fechaNac = fields.Date(string="Fecha nacimiento", required = True)
    
    direccion = fields.Char(string="Dirección", required = True)
    
    telefono = fields.Char(string="Teléfono", required = True)
    
    foto = fields.Boolean(string="Imagen", compute="_compute_foto") 
    
    fotoAlumno = fields.Char(string="Image URL")

    email = fields.Char(string="Email")
    
    asignatura = fields.Many2many("instituto.asignatura", string="Asignaturas")
    
    calificaciones = fields.One2many("instituto.calificacion", "estudiante", string="Calificaciones")

    grupo = fields.Many2one("instituto.grupo", string="Grupo")


    _sql_constraints = [
        ('dni_unique', 'unique(name)', 'El DNI debe ser único.'),
    ]

    @api.depends('fotoAlumno')
    def _compute_foto(self):
        for record in self:
            record.foto = True if record.fotoAlumno else False

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

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError('El correo electrónico debe ser válido.')

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
            
    

            

