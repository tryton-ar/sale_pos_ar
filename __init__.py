# This file is part sale_pos_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import configuration
from . import sale

__all__ = ['register']


def register():
    Pool.register(
        configuration.Configuration,
        configuration.ConfigurationPos,
        sale.Sale,
        module='sale_pos_ar', type_='model')
