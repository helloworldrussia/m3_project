from itertools import imap
from collections import namedtuple

from django.db.models.query import ValuesQuerySet


class NamedTuplesQuerySet(ValuesQuerySet):
    def iterator(self):
        # собираем список имён полей
        extra_names = self.query.extra_select.keys()
        field_names = self.field_names
        aggregate_names = self.query.aggregate_select.keys()
        names = extra_names + field_names + aggregate_names

        # создаём класс кортежа
        tuple_cls = namedtuple('%sTuple' % self.model.__name__, names)

        results_iter = self.query.get_compiler(self.db).results_iter()
        # заворачиваем каждую строку в наш именованный кортеж
        return imap(tuple_cls._make, results_iter)