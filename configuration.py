# The COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']


class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'sale.configuration'
    pos = fields.Property(fields.Many2One('account.pos', 'Point of sale',
            domain=[('pos_daily_report', '=', False)],
            required=True,
            help='The point of sale to be '
            'used when the invoice is created.'))
