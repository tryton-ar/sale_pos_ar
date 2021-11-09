# The COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.
from trytond import backend
from trytond.model import fields, ModelSQL
from trytond.pool import PoolMeta, Pool
from trytond.tools.multivalue import migrate_property
from trytond.modules.company.model import CompanyValueMixin


class Configuration(metaclass=PoolMeta):
    __name__ = 'sale.configuration'
    pos = fields.MultiValue(fields.Many2One(
            'account.pos', "Point of Sale", required=True,
            domain=[
                ('pos_daily_report', '=', False)
                ]))

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field == 'pos':
            return pool.get('sale.configuration.pos')
        return super().multivalue_model(field)


class ConfigurationPos(ModelSQL, CompanyValueMixin):
    "Sale Configuration Pos"
    __name__ = 'sale.configuration.pos'
    pos = fields.Many2One(
        'account.pos', "Point Of Sale", required=True,
        domain=[
            ('pos_daily_report', '=', False)
            ],
        depends=['company'])

    @classmethod
    def __register__(cls, module_name):
        exist = backend.TableHandler.table_exist(cls._table)
        super().__register__(module_name)
        if not exist:
            cls._migrate_property([], [], [])

    @classmethod
    def _migrate_property(cls, field_names, value_names, fields):
        field_names.append('pos')
        value_names.append('pos')
        fields.append('company')
        migrate_property(
            'sale.configuration', field_names, cls, value_names,
            fields=fields)
