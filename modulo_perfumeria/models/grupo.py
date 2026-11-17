from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Grupos(models.Model):
    _name = "modulo_perfumeria.grupo"
    _description = "Gama del perfume"

    nombre = fields.Char(string="Nombre del Grupo", required=True)
    descripcion = fields.Text(string="Descripcion")
    activo = fields.Boolean(string="Activo", default=True)

    gama = fields.Selection([
        ('baja', 'BAJA'),
        ('media', 'MEDIA'),
        ('alta', 'ALTA')
    ], string="Gama", default='media')

    familiaOlfativa = fields.Selection([
        ('floral', 'Floral'),
        ('amaderada', 'Amaderada'),
        ('citrica', 'Citrica'),
        ('oriental', 'Oriental')
    ], string="Familia Olfativa", default='floral')

    coleccion = fields.Selection([
        ('clasica', 'Clasica'),
        ('estacional', 'Estacional'),
        ('edicion_limitada', 'Edicion Limitada')
    ], string="Coleccion", default='clasica')

    publico = fields.Selection([
        ('hombres', 'Hombres'),
        ('mujeres', 'Mujeres'),
        ('unisex', 'Unisex')
    ], string="Publico", default='unisex')

    imagen = fields.Binary(string="Imagen de Gama")
    fechaCreacion = fields.Date(string="Fecha de Creacion", default=fields.Date.today)
    fechaRegistro = fields.Datetime(string="Fecha de Registro", default=fields.Datetime.now)

    perfume_ids = fields.One2many(
        'modulo_perfumeria.perfume',
        'grupo_id',
        string="Perfumes"
    )

    valor_total_grupo = fields.Float(
        string="Valor Total Grupo",
        compute="_compute_valor_total_grupo",
        store=True
    )

    @api.depends('perfume_ids.precioPerfume')
    def _compute_valor_total_grupo(self):
        for grupo in self:
            grupo.valor_total_grupo = sum(perfume.precioPerfume for perfume in grupo.perfume_ids)

    @api.constrains('fechaCreacion')
    def _check_fecha_creacion(self):
        for record in self:
            if record.fechaCreacion and record.fechaCreacion > fields.Date.today():
                raise ValidationError("La fecha de creacion no puede ser una fecha futura.")

    @api.constrains('nombre')
    def _check_nombre(self):
        for record in self:
            if record.nombre and len(record.nombre.strip()) < 3:
                raise ValidationError("El nombre del grupo debe tener al menos 3 caracteres.")
