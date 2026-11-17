from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Perfumes(models.Model):
    _name = "modulo_perfumeria.perfume"
    _description = "Clase de Perfume"

    nombrePerfume = fields.Char(string="Nombre Perfume", required=True)
    marcaPerfume = fields.Char(string="Marca Perfume", required=True)
    precioPerfume = fields.Float(string="Precio Base", required=True, default=0.0)
    stock = fields.Integer(string="Stock", default=0)
    observacionesPefume = fields.Text(string="Observaciones")
    disponible = fields.Boolean(string="Disponible", default=True)

    imagen = fields.Binary(string="Foto")
    fechaLanzamiento = fields.Date(string="Fecha de Lanzamiento")
    fechaRegistro = fields.Datetime(string="Fecha de Registro", default=fields.Datetime.now)

    tipoPerfume = fields.Selection([
        ('colonia', 'Agua de Colonia (EDC)'),
        ('edt', 'Eau de Toilette (EDT)'),
        ('edp', 'Eau de Parfum (EDP)'),
        ('extracto', 'Extracto de Perfume')
    ], string="Tipo de Perfume", default='edt')

    precio_con_iva = fields.Float(
        string="Precio con IVA",
        compute="_compute_precio_con_iva",
        store=True
    )

    grupo_id = fields.Many2one('modulo_perfumeria.grupo', string="Grupo")
    tienda_id = fields.Many2one('modulo_perfumeria.tienda', string="Tienda")
    cliente_ids = fields.Many2many('modulo_perfumeria.cliente', string="Clientes")

    @api.depends('precioPerfume')
    def _compute_precio_con_iva(self):
        for record in self:
            if record.precioPerfume < 0:
                raise ValidationError("El precio del perfume no puede ser negativo.")
            record.precio_con_iva = record.precioPerfume * 1.21

    @api.constrains('precioPerfume')
    def _check_precio_unitario(self):
        for record in self:
            if record.precioPerfume <= 0:
                raise ValidationError("El precio unitario debe ser mayor que 0.00.")

    @api.constrains('fechaLanzamiento')
    def _check_fecha_lanzamiento(self):
        for record in self:
            if record.fechaLanzamiento and record.fechaLanzamiento > fields.Date.today():
                raise ValidationError("La fecha de lanzamiento no puede ser una fecha futura.")

    @api.onchange('tipoPerfume')
    def _onchange_tipo_perfume(self):
        if self.tipoPerfume == 'extracto':
            self.observacionesPefume = "Fragancia de extracto puro. Aplicar poca cantidad."
        elif self.tipoPerfume == 'colonia':
            self.observacionesPefume = "Agua de colonia fresca para uso diario."
        else:
            self.observacionesPefume = False
