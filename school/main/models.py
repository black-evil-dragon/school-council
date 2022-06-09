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

class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Содержимое')
    date = models.DateField(_("Date"), default=datetime.now, blank=True)
    time = models.TimeField(default=default_start_time)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
