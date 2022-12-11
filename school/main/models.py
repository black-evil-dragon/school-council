# models.py

from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime, timedelta


def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)

class Post(models.Model):
    creator = models.CharField('Автор', max_length=50)
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Содержимое')
    date = models.DateField(_('Дата'), default=datetime.now, blank=True)
    time = models.TimeField('Время', default=default_start_time)

    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class AboutSchool(models.Model):
    id = models.PositiveIntegerField('Порядковый номер', primary_key=True, unique=True)
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Содержимое')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Описание школы'
        verbose_name_plural = 'Описание школы'


class Contacts(models.Model):
    text = models.TextField('Содержимое')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

class WidgetLinks(models.Model):
    id = models.AutoField(primary_key=True)
    gradients = [
        ('blue-white', 'Синий-белый'),
        ('red-white', 'Красный-белый'),
        ('green-white', 'Зелёный-белый'),
        ('purple-orange', 'Фиолетовый-бежевый')
    ]

    title = models.CharField('Заголовок', max_length=50, default='')
    link = models.CharField('Ссылка', max_length=200, default='')
    gradient = models.CharField('Градиент', choices=gradients, default='blue-white', max_length=20)

    image = models.ImageField('Смайл', upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Виджет'
        verbose_name_plural = 'Виджеты'
