from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Tiendas(models.Model):
    _name = "modulo_perfumeria.tienda"
    _description = "Tiendas de la empresa"

    nombreTienda = fields.Char(string="Nombre Tienda", required=True)
    direccionTienda = fields.Char(string="Direccion", required=True)
    telefonoTienda = fields.Char(string="Telefono")
    observacionesTienda = fields.Text(string="Observaciones")
    abierta = fields.Boolean(string="Tienda Abierta", default=True)

    tipoTienda = fields.Selection([
        ('local', 'Local Propio'),
        ('sucursal', 'Sucursal'),
        ('flagship', 'Tienda Principal')
    ], string="Tipo de Tienda", default='local')

    fotoTienda = fields.Binary(string="Foto de la Tienda")
    fechaInauguracion = fields.Date(string="Fecha Inauguracion")
    fechaUltimaRevision = fields.Datetime(string="Ultima Revision", default=fields.Datetime.now)

    perfume_ids = fields.One2many(
        'modulo_perfumeria.perfume',
        'tienda_id',
        string="Catalogo de Perfumes"
    )

    @api.constrains('fechaInauguracion')
    def _check_fecha_inauguracion(self):
        for record in self:
            if record.fechaInauguracion and record.fechaInauguracion > fields.Date.today():
                raise ValidationError("La fecha de inauguracion no puede ser una fecha futura.")
