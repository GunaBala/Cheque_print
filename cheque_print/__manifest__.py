# -*- encoding: utf-8 -*-

{
    'name': 'Dynamic Cheque Printing',
    'version': '11.0.1.1',
    'sequence': 150,
    'category': 'Accounts',
    'summary': 'Cheque Print',
    'description': """ Cheque Print """,
    'author': 'Future Dev',
    'website': '',
    'license': 'LGPL-3',
    'price': '12',
    'currency':'EUR',
    'depends': ['account','web'],
    'init_xml': [],
    'data': [
            'security/ir.model.access.csv',
            'wizard/wizard_cheque_print_view.xml',
            'views/cheque_report.xml',
            'views/data.xml',
            'views/cheque_print_config_view.xml',
           ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
