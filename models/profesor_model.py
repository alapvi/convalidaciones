# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class profesor_model(models.Model):
    _name='convalidaciones.profesor_model'
    _description = 'Modelo de Profesores'


    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre")
    apellidos =fields.Char(string="Apellidos",required=True,index=True,help="Apellidos")
    foto=fields.Binary()
    dni=fields.Char(string="DNI",required=True,size=9,help="DNI")
    alumnos = fields.Many2many("convalidaciones.alumno_model",string="Alumnos")
            
    
