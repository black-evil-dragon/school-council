# Generated by Django 4.0.4 on 2022-09-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
            ],
            options={
                'verbose_name': 'Описание школы',
                'verbose_name_plural': 'Описание школы',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
    ]
