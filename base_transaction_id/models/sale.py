# -*- coding: utf-8 -*-
#
#    Author: Nicolas Bessi, Yannick Vaucher
#    Copyright 2011-2015 Camptocamp SA
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
from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    transaction_id = fields.Char(
        'Transaction ID',
        required=False,
        copy=False,
        help="Transaction id from the financial institute"
    )

    @api.multi
    def _prepare_invoice(self):
        """ Propagate the transaction_id from the sale order to the invoice """
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['transaction_id'] = self.transaction_id
        return invoice_vals