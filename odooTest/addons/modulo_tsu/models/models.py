# -*- coding: utf-8 -*-
from django.db.models.expressions import result
from odoo import models, fields, api


class modulo_tsu(models.Model):
    _name = 'modulo_tsu.modulo_tsu'
    _description = 'modulo_tsu.modulo_tsu'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class Curso(models.Model):
    _name = "modulo_tsu.curso"
    _description = "Modelo para gestionar cursos académicos"
    idCurso = fields.Char(
        string="Código del Curso",
        required=True,
        size = 6,
        unique = True
    )
    nombre = fields.Char(
        string="Nombre del curso",
        required=True,
        size=60
    )
    creditos = fields.Integer(
        string="Creditos",
        required=True
    )
    
    _sql_constrains = [
        ('idCurso', 'UNIQUE(idCurso)', 'El id debe ser unico')
    ]

    def name_get(self):
        result = []
        for curso in self:
            result.append((curso.idCurso, f"{curso.nombre} ({curso.creditos})"))
        return result

