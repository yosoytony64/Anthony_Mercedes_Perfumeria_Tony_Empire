from odoo import models, fields

class Perfumes(models.Model):

    _name ="modulo_perfumeria.perfume"

    _description = "Clase de perfume"

    nombrePerfume= fields.Char(string="Nombre Perfume", required=True, help="Nombre del Perfume")

    marcaPerfume = fields.Char(string="Marca Perfume", required=True, help="Marca del Perfume")

    precioPerfume = fields.Integer(string="Precio Perfume", help="Precio del Perfume")
    
    observacionesPefume = fields.Char(string="Observaciones Perfume", help="Observaciones del Perfume")

    tipoPerfume = fields.Selection([('edt','EDT'),('edp','EDP'),('extracto','EXTRACTO')],string="Tipo_de_Perfume")

    grupo_id = fields.Many2one('modulo_perfumeria.grupo', string='Grupos')

    