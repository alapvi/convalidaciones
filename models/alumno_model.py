# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class alumno_model(models.Model):
    _name='convalidaciones.alumno_model'
    _description = 'Modelo de alumnos'


    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre del alumno")
    foto=fields.Binary()
    password=fields.Char(string="Password",size=10,help="Password del alumno")
    edad=fields.Integer(string="Edad",required=True,help="Edad del alumno")
    localidad=fields.Char(string="Localidad",size=100,required=True,help="Localidad del alumno")
    provincia=fields.Char(string="Provincia",size=100,required=True,help="Provincia del alumno")
    email=fields.Char(string="Email",size=100,required=False,help="Email del alumno")


    def generarPassword(self):
        self.password=""
        self.ensure_one()
        for i in range (10):
            self.password+=random.choice("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
        return True    
            
