from . import models
from odoo import api, SUPERUSER_ID


def _post_init_hook(cr, registry):
    """ Make Jordan companies use round globally """
    env = api.Environment(cr, SUPERUSER_ID, {})
    jordan_chart_id = env.ref('l10n_jo.jor_chart_template_standard')
    if jo_companies := env['res.company'].search([('chart_template_id', '=', jordan_chart_id.id)]):
        for company in jo_companies:
            company.tax_calculation_rounding_method = 'round_globally'
