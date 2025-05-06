# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models


class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    def _load_template(self, company, code_digits=None, account_ref=None, taxes_ref=None):
        account_ref, taxes_ref = super(AccountChartTemplate, self)._load_template(company=company,
                                                                                  code_digits=code_digits,
                                                                                  account_ref=account_ref,
                                                                                  taxes_ref=taxes_ref)
        if self == self.env.ref('l10n_jo.jor_chart_template_standard'):
            self.env.ref('l10n_jo.jo_tax_group_16').write({
                'property_tax_payable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200906')),
                'property_tax_receivable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200905')),
            })
            self.env.ref('l10n_jo.jo_tax_group_10').write({
                'property_tax_payable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200906')),
                'property_tax_receivable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200905')),
            })
            self.env.ref('l10n_jo.jo_tax_group_4').write({
                'property_tax_payable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200906')),
                'property_tax_receivable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200905')),
            })
            self.env.ref('l10n_jo.jo_tax_group_0').write({
                'property_tax_payable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200906')),
                'property_tax_receivable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200905')),
            })
            self.env.ref('l10n_jo.jo_tax_group_exempt').write({
                'property_tax_payable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200906')),
                'property_tax_receivable_account_id': account_ref.get(self.env.ref('l10n_jo.jo_account_200905')),
            })
        return account_ref, taxes_ref
