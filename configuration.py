# This file is part sale_pos_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import fields, ModelSQL
from trytond.pool import PoolMeta, Pool
from trytond.modules.company.model import CompanyValueMixin


class Configuration(metaclass=PoolMeta):
    __name__ = 'sale.configuration'

    pos = fields.MultiValue(fields.Many2One(
        'account.pos', "Point of Sale", required=True,
        domain=[('pos_daily_report', '=', False)]))

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field == 'pos':
            return pool.get('sale.configuration.pos')
        return super().multivalue_model(field)


class ConfigurationPos(ModelSQL, CompanyValueMixin):
    "Sale PoS Configuration"
    __name__ = 'sale.configuration.pos'

    pos = fields.Many2One('account.pos', "Point of Sale", required=True,
        domain=[('pos_daily_report', '=', False)],
        depends={'company'})
