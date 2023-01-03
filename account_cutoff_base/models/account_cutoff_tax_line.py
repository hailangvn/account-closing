# Copyright 2013-2021 Akretion (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountCutoffTaxLine(models.Model):
    _name = "account.cutoff.tax.line"
    _inherit = "analytic.mixin"
    _description = "Account Cut-off Tax Line"

    parent_id = fields.Many2one(
        "account.cutoff.line",
        string="Account Cut-off Line",
        ondelete="cascade",
        required=True,
    )
    tax_id = fields.Many2one("account.tax", string="Tax", required=True)
    cutoff_account_id = fields.Many2one(
        "account.account",
        string="Cut-off Account",
        required=True,
        readonly=True,
    )
    base = fields.Monetary(
        currency_field="currency_id",
        readonly=True,
        help="Base Amount in the currency of the PO.",
    )
    amount = fields.Monetary(
        string="Tax Amount",
        currency_field="currency_id",
        readonly=True,
        help="Tax Amount in the currency of the PO.",
    )
    sequence = fields.Integer(readonly=True)
    cutoff_amount = fields.Monetary(
        string="Cut-off Tax Amount",
        currency_field="company_currency_id",
        readonly=True,
        help="Tax Cut-off Amount in the company currency.",
    )
    currency_id = fields.Many2one(
        related="parent_id.currency_id", string="Currency", readonly=True
    )
    company_currency_id = fields.Many2one(
        related="parent_id.company_currency_id",
        string="Company Currency",
        readonly=True,
    )
