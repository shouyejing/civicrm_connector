##############################################################################
#
#    SEPA Direct Debit module for OpenERP
#    Copyright (C) 2013 Akretion (http://www.akretion.com)
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
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
{
    'name': 'SP Account Banking SEPA Direct Debit',
    'summary': 'Create SEPA files for Direct Debit',
    'version': '0.1',
    'license': 'AGPL-3',
    'author': 'Akretion (customized by B-Informed & Smart Solution)',
    'website': 'http://www.b-informed.nl',
    'category': 'Banking addons',
    'depends': ['account_direct_debit', 'account_banking_pain_base', 'account_payment'],
    'external_dependencies': {
        'python': ['unidecode', 'lxml'],
        },
    'data': [
        'security/original_mandate_required_security.xml',
        'account_banking_sdd_view.xml',
        'sdd_mandate_view.xml',
#        'res_partner_bank_view.xml',
        'account_payment_view.xml',
        'company_view.xml',
        'account_journal_view.xml',
        'payment_mode.xml',
        'mandate_expire_cron.xml',
        'account_invoice_view.xml',
        'wizard/export_sdd_view.xml',
        'data/payment_type_sdd.xml',
        'data/mandate_reference_sequence.xml',
        'data/ir_config_parameter.xml',
        'res_config_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['sepa_direct_debit_demo.xml'],
    'description': '''
Module to export direct debit payment orders in SEPA XML file format.

SEPA PAIN (PAyment INitiation) is the new european standard for Customer-to-Bank payment instructions. This module implements SEPA Direct Debit (SDD), more specifically PAIN versions 008.001.02, 008.001.03 and 008.001.04. It is part of the ISO 20022 standard, available on http://www.iso20022.org.

The Implementation Guidelines for SEPA Direct Debit published by the European Payments Council (http://http://www.europeanpaymentscouncil.eu) use PAIN version 008.001.02. So if you don't know which version your bank supports, you should try version 008.001.02 first.

This module uses the framework provided by the banking addons, cf https://launchpad.net/banking-addons
    ''',
    'active': False,
    'installable': True,
}
