from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Clientes(models.Model):
    _name = "modulo_perfumeria.cliente"
    _description = "Clientes de la perfumeria"

    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    email = fields.Char(string="Email")
    esSocio = fields.Boolean(string="Es Socio", default=False)
    notas = fields.Text(string="Notas del Cliente")

    tipoCliente = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('ocasional', 'Ocasional'),
        ('vip', 'VIP')
    ], string="Tipo de Cliente", default='nuevo')

    foto = fields.Binary(string="Foto de Perfil")
    fechaNacimiento = fields.Date(string="Fecha de Nacimiento")
    fechaAlta = fields.Datetime(string="Fecha de Alta", default=fields.Datetime.now)

    perfume_ids = fields.Many2many(
        'modulo_perfumeria.perfume',
        string="Perfumes Guardados"
    )

    @api.onchange('tipoCliente')
    def _onchange_tipo_cliente(self):
        if self.tipoCliente == 'vip':
            self.esSocio = True
            self.notas = "Cliente VIP: Aplica trato preferente y descuentos especiales."
        else:
            self.esSocio = False
            self.notas = False

    @api.constrains('fechaNacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fechaNacimiento and record.fechaNacimiento > fields.Date.today():
                raise ValidationError("La fecha de nacimiento no puede ser una fecha futura.")
