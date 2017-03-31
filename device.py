# This file is part of the sale_pos_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['SaleDevice']
__metaclass__ = PoolMeta


class SaleDevice:
    __name__ = 'sale.device'
    pos_ar = fields.Many2One('account.pos', 'Point of Sale')
