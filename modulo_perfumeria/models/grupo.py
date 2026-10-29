from odoo import models, fields

class Grupos(models.Model):
    _name = "modulo_perfumeria.grupo"
    _description = "Gama del perfume"

    nombre = fields.Char(string="Nombre del Grupo", required=True)

    gama = fields.Selection([('baja','BAJA'),('media','MEDIA'),('alta','ALTA')],string="Gama")

    familiaOlfativa = fields.Selection([('floral','Floral'),('amaderada','Amaderada'),('cítrica','Cítrica')],string="Familia Olfativa")

    coleccion = fields.Selection([('clásica','Clásica'),('estacional','Estacional'),('edición_limitada','Edición_limitada')],string="Coleccion")

    publico = fields.Selection([('hombres','Hombres'),('mujeres','Mujeres'),('unisex','Unisex')], string="publico")

    perfume_ids = fields.One2many('modulo_perfumeria.perfume','grupo_id',string='Perfumes')