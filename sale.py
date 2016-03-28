# coding=utf-8
#This file is part of the sale_pos_ar module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    pos = fields.Many2One(
        'account.pos', 'Point of Sale',
        states={
            'readonly': Eval('state') != 'draft',
        },
        depends=['state'])
    invoice_type = fields.Many2One(
        'account.pos.sequence', 'Invoice Type',
        states={
            'readonly': Eval('state') != 'draft',
        },
        domain=([('pos', '=', Eval('pos'))]),
        depends=['state'])

    @staticmethod
    def default_pos():
        Configuration = Pool().get('sale.configuration')
        config = Configuration(1)
        if config.pos:
            return config.pos.id

    def create_invoice(self, invoice_type):
        invoice = super(Sale, self).create_invoice(invoice_type)
        if invoice:
            invoice.pos = self.pos
            invoice.invoice_type = self.invoice_type
            invoice.pyafipws_concept = self.get_pyafipws_concept()
            if invoice.pyafipws_concept == '2' or invoice.pyafipws_concept == '3':
                invoice.pyafipws_billing_start_date, invoice.pyafipws_billing_end_date = self.get_pyafipws_billings_date()
            invoice.save()
        return invoice

    def get_pyafipws_concept(self):
        products = {'1': 0, '2': 0}
        for line in self.lines:
            if line.product.type == 'goods':
                products['1'] += 1
            if line.product.type == 'service':
                products['2'] += 1

        if products['1'] != 0 and products['2'] != 0:
            return '3'
        elif products['1'] != 0:
            return '1'
        elif products['2'] != 0:
            return '2'
        else:
            return ''

    def get_pyafipws_billings_date(self):
        import calendar
        import datetime
        year = int(datetime.date.today().strftime("%Y"))
        month = int(datetime.date.today().strftime("%m"))
        monthrange = calendar.monthrange(year, month)
        start_date = datetime.date(year, month, 1)
        end_date = datetime.date(year, month, monthrange[1])
        return (start_date, end_date)
