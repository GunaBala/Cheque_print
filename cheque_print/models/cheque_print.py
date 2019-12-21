# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-TODAY ePillars Systems LLC (<http://www.epillars.com>)
#    Copyright (C) 2004 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from odoo import models,fields

class cheque_print(models.Model):
    _name = "cheque.print"
    _description = "Cheque Printing"
    
    name = fields.Char('Name')
    main_left = fields.Integer('Main Left')
    main_top = fields.Integer('Main Top')
    
    date_padding_top = fields.Integer('Margin Top %')
    date_padding_left = fields.Integer('Margin Left %')
    date_font_size = fields.Integer('Font Size')
    
    partner_padding_top = fields.Integer('Margin Top %')
    partner_padding_left = fields.Integer('Margin Left %')
    partner_font_size = fields.Integer('Font Size')
    
    words_padding_top = fields.Integer('Margin Top %')
    words_padding_left = fields.Integer('Margin Left %')
    words_font_size = fields.Integer('Font Size')
    words_width = fields.Integer('Width')
    words_line_height = fields.Integer('Line Height')
    
    amount_padding_top = fields.Integer('Margin Top %')
    amount_padding_left = fields.Integer('Margin Left %')
    amount_font_size = fields.Integer('Font Size')

    def get_main_style(self,cheque_id):
        if cheque_id:
            val = self.env['cheque.print'].browse(cheque_id)
            style = 'top:%s;left:%s;position:absolute;width:100%%;height:100%%' % (val.main_top,val.main_left)
            return style

    def get_date_style(self,cheque_id):
        if cheque_id:
            val = self.env['cheque.print'].browse(cheque_id)
            style = 'padding-top:%s%%;padding-left:%s%%;font-size:%s;position:absolute;font-weight:bold'\
                    % (val.date_padding_top,val.date_padding_left,val.date_font_size)
            return style

    def get_partner_style(self,cheque_id):
        if cheque_id:
            val = self.env['cheque.print'].browse(cheque_id)
            style = 'padding-top:%s%%;padding-left:%s%%;font-size:%s;position:absolute;font-weight:bold;overflow:auto'\
                    % (val.partner_padding_top,val.partner_padding_left,val.partner_font_size)
            return style

    def get_words_style(self,cheque_id):
        if cheque_id:
            val = self.env['cheque.print'].browse(cheque_id)
            style = 'padding-top:%s%%;padding-left:%s%%;font-size:%s;width:%s%%;line-height:%s%%;position:absolute;font-weight:bold;'\
                    % (val.words_padding_top,val.words_padding_left,val.words_font_size,val.words_width,val.words_line_height)
            return style

    def get_amount_style(self,cheque_id):
        if cheque_id:
            val = self.env['cheque.print'].browse(cheque_id)
            style = 'padding-top:%s%%;padding-left:%s%%;font-size:%s;position:absolute;font-weight:bold;'\
                    % (val.amount_padding_top,val.amount_padding_left,val.amount_font_size)
            return style
        


class AccountPayment(models.Model):
    _inherit = "account.payment"
    
    cheque_number = fields.Integer(string="Check Number", copy=False)
