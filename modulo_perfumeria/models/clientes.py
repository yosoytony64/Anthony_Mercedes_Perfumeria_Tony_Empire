from odoo import models, fields

class Vips(models.Model):

    nombre =  fields.Char(string="Nombre Cliente", required=True, help="Nombre del Cliente")

    apellido =  fields.Char(string="Apellido  Cliente", required=True, help="Apellido del Cliente")

    tipoCliente = fields.Selection([('nuevo','Nuevo'),('ocasional','Ocasional'),('vip','Vip')],string="Tipo_de_Perfume")

    
