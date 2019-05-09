#Model de notre Module Keyfa Aboo

from odoo import models, fields, api

class Keyfaaboo_template(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    choixtissu = fields.Boolean('Avec Tissu')
    choixmodele = fields.Selection(selection=[('mk','MKO'), ('mb', 'Marabout'), ('ar', 'Art')], string="Modele ")
    choixcouleur = fields.Selection(selection=[('rg', 'Rouge'), ('rs', 'Rose'), ('bl', 'Bleu')], string="Couleur ")
    choixbroderie = fields.Selection(selection=[('rg', 'Rouge'), ('rs', 'Rose'), ('bl', 'Bleu')], string="Broderie ")

class Keyfaaboo_production_template(models.Model):
    _name = 'mrp.production'
    _inherit = 'mrp.production'

    choixtissu = fields.Boolean('Avec Tissu', compute='_compute_champs')
    choixmodele = fields.Selection(selection=[('mk', 'MKO'), ('mb', 'Marabout'), ('ar', 'Art')], string="Modele ", compute='_compute_champs')
    choixcouleur = fields.Selection(selection=[('rg', 'Rouge'), ('rs', 'Rose'), ('bl', 'Bleu')], string="Couleur ", compute='_compute_champs')
    choixbroderie = fields.Selection(selection=[('rg', 'Rouge'), ('rs', 'Rose'), ('bl', 'Bleu')], string="Broderie ", compute='_compute_champs')

    @api.multi
    def _compute_champs(self):
        def get_parent_move(move):
            if move.move_dest_id:
                return get_parent_move(move.move_dest_id)
            return move

        for production in self:
            move = get_parent_move(production.move_finished_ids[0])
            production.choixtissu = move.procurement_id and move.procurement_id.sale_line_id and move.procurement_id.sale_line_id.choixtissu or False
            production.choixmodele = move.procurement_id and move.procurement_id.sale_line_id and move.procurement_id.sale_line_id.choixmodele or False
            production.choixcouleur = move.procurement_id and move.procurement_id.sale_line_id and move.procurement_id.sale_line_id.choixcouleur or False
            production.choixbroderie = move.procurement_id and move.procurement_id.sale_line_id and move.procurement_id.sale_line_id.choixbroderie or False