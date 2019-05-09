from odoo import models, fields, api

class Clientkeyfa(models.Model):

    _name = 'res.partner'
    _inherit = 'res.partner'

    name = fields.Char(string="Nom", required=False, )


