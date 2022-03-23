# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 15 pour J Cloture',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 15 pour J Cloture
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'sale_management',
        'sales_team',
        'mail',
        'account',
        'purchase',
],
    'data' : [
        'views/partner_view.xml',
        'report/sale_report_templates.xml',
        'report/report_invoice.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
    'license': 'LGPL-3',
}

