# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Jordan - Accounting',
    'countries': ['jo'],
    'description': """
This is the base module to manage the accounting chart for Jordan in Odoo.
==============================================================================

Jordan accounting basic charts and localization.

Activates:

- Chart of accounts

- Taxes

- Tax report

- Fiscal positions
    """,
    'category': 'Accounting/Localizations/Account Charts',
    'version': '1.0',
    'depends': [
        'account',
    ],
    'data': [
        'data/l10n_jor_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_group_data.xml',
        'data/l10n_jor_chart_post_data.xml',
        'data/account_account_tag.xml',
        'data/account_tax_template_data.xml',
        'data/account_fiscal_position_templates_data.xml',
        'data/account_chart_template_data.xml',
        'views/account_move.xml',
        'data/account.group.template.csv',
        # 'data/account_tax_report_data.xml',
    ],
    'demo': [
        # 'demo/demo_company.xml',
        # 'demo/demo_partner.xml',
    ],
    'license': 'LGPL-3',
}
