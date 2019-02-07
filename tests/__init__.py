# The COPYRIGHT file at the top level of jhis repository contains the
# full copyright notices and license terms.

try:
    from trytond.modules.sale_pos_ar.tests.test_sale_pos_ar import suite
except ImportError:
    from .test_sale_pos_ar import suite

__all__ = ['suite']
