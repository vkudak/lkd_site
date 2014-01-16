# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ';')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value, *args, **kwargs):
        if not value:
            return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class ObsType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип спостережень')

    class Meta:
        verbose_name = 'Типи спостережень' # Множина
        verbose_name_plural = 'Тип спостережень'  # однина

    def __unicode__(self):
        return self.name


# def get_upload_to(instance, filename):
#     #my_custom_date = datetime.now()
#     #date = unicode(instance)
#     date = instance
#     date = date.split()[0]
#     date = date.split('-')
#     if len(date) != 3:
#         date = date.split('/')
#     return '%s/%s/%s/%s' % (date[0], date[1], date[2], filename)


class Obs(models.Model):
    date = models.DateTimeField(auto_now_add=False, verbose_name='Дата створення')
    description = models.TextField(verbose_name='Опис')
    # content = models.FileField(verbose_name='Файл', upload_to=get_upload_to)
    content = SeparatedValuesField()
    category = models.ForeignKey(ObsType, related_name='Тип', verbose_name='Тип')
    user = models.ForeignKey(User, verbose_name='Користувач')

    class Meta:
        verbose_name = 'Ніч спостережень'
        verbose_name_plural = 'Спостереження'

    def __unicode__(self):
        return unicode(self.date)