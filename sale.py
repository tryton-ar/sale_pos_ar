# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'
    pos = fields.Many2One('account.pos', 'Point of Sale',
        domain=[('pos_daily_report', '=', False)],
        states={
            'readonly': Eval('state') != 'draft',
        },
        depends=['state'])

    @staticmethod
    def default_pos():
        Configuration = Pool().get('sale.configuration')
        config = Configuration(1)
        if config.pos:
            return config.pos.id

    def create_invoice(self):
        invoice = super().create_invoice()
        if invoice:
            invoice.pos = self.pos
            invoice.invoice_type = invoice.on_change_with_invoice_type()
            invoice.set_pyafipws_concept()
            invoice.set_pyafipws_billing_dates()
            invoice.save()
        return invoice
