# Generated by Django 4.0 on 2022-01-06 15:46

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('time', models.TimeField(default=main.models.default_start_time)),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('cover', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
