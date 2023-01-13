# Copyright 2023 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Informe Contabilidad Munin',
    'description': """
        Reporte de factura para munin""",
    'version': '16',
    'license': 'AGPL-3',
    'author': 'Munin',
    'depends': ['base', 'account', 'l10n_mx_edi', 'l10n_mx'
                ],
    'data': [
        "report/invoice_report.xml",
    ],
    'demo': [
    ],
}
