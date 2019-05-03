# This file is part sale_pos_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import sale
from . import configuration


def register():
    Pool.register(
        sale.Sale,
        configuration.Configuration,
        configuration.ConfigurationPos,
        module='sale_pos_ar', type_='model')
