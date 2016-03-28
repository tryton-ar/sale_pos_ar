#This file is part sale_pos_ar module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .sale import *
from .configuration import *


def register():
    Pool.register(
        Sale,
        Configuration,
        module='sale_pos_ar', type_='model')
