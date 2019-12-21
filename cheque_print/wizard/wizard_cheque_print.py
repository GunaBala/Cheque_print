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

class wizard_cheque_print(models.TransientModel):
    _name = "wizard.cheque.print"
    _description = "Wizard for Cheque selection"
    
    cheque_id = fields.Many2one('cheque.print','Cheque Name')
    
    def print_cheque(self):
        active_id = self.env.context.get('active_id')
        datas = {
             'ids': [],
             'model': self.env.context.get('active_model'),
             'active_id': active_id,
             'cheque_id':self.cheque_id.id
        }
        
        docs = self.env[datas['model']].browse(datas['active_id'])
        if self.env.context.get('active_model') == 'account.payment':
            return self.env.ref('cheque_print.report_account_payment_cheque_print').report_action(docs,data=datas)

            
 
