# Generated by Django 3.1.7 on 2021-06-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210505_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=100, verbose_name='Фамилия пользователя'),
        ),
    ]
