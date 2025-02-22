# -*- coding: utf-8 -*-

from odoo import models, fields, api


class asignatura(models.Model):
     _name = 'instituto.asignatura'
     _description = 'instituto.asignatura'

     name = fields.Char(string="Nombre", required=True)
     curso = fields.Many2one("instituto.curso", string="Curso", required=True)
     estudiantes = fields.Many2many("instituto.estudiante", string="Estudiantes", required=True, readonly=True)
     
     def name_get(self):
        result = []
        for record in self:
            name = f"{record.name} ({record.curso.name}º curso)" if record.curso else record.name
            result.append((record.id, name))
        return result
