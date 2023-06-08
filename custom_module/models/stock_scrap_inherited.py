from odoo import fields, models


class StockScrapInherited(models.Model):
    _inherit = 'stock.scrap'

    origin = fields.Char(string="Source of Failure")

