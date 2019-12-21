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

from datetime import date, datetime

from odoo import api, models, _
from odoo.exceptions import UserError
from num2words import num2words

class cheque_print(models.AbstractModel):
    _name = 'report.cheque_print.report_cheque_print_template'
    
    @api.model
    def get_report_values(self, docids, data=None):
        docs = self.env[data['model']].browse(data['active_id'])
        cheque_print = self.env['cheque.print']
    
        get_main_style = cheque_print.get_main_style(data['cheque_id'])
        get_date_style = cheque_print.get_date_style(data['cheque_id'])
        get_partner_style = cheque_print.get_partner_style(data['cheque_id'])
        get_words_style = cheque_print.get_words_style(data['cheque_id'])
        get_amount_style = cheque_print.get_amount_style(data['cheque_id'])
        partner_name = docs.partner_id.name
        docargs = {
            'doc_ids': docids,
            'doc_model': data['model'],
            'data': data,
            'docs': docs,
            'get_date_style': get_date_style,
            'get_main_style': get_main_style,
            'get_partner_style': get_partner_style,
            'get_words_style': get_words_style,
            'get_amount_style': get_amount_style,
            'payment_date':docs.payment_date,
            'partner_id':partner_name,
            'amount':docs.amount,
            'amount_in_words':docs.currency_id.amount_to_text(docs.amount),

        }
        return docargs

