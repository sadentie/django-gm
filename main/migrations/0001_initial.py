# Generated by Django 4.1.7 on 2023-08-06 23:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanseledGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=250, verbose_name='Цель')),
                ('timespend', models.IntegerField(verbose_name='Времени потрачено')),
            ],
            options={
                'verbose_name': 'Отмененная цель',
                'verbose_name_plural': 'Отмененные цели',
            },
        ),
        migrations.CreateModel(
            name='CompletedGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=250, verbose_name='Цель')),
                ('timespend', models.IntegerField(verbose_name='Времени потрачено')),
                ('enddate', models.DateField(verbose_name='Дата окончания')),
                ('user', models.CharField(default=None, max_length=250, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Законченная цель',
                'verbose_name_plural': 'Законченные цели',
            },
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=250, verbose_name='Цель')),
                ('datestart', models.DateField(default=datetime.date.today, verbose_name='Дата начала цели')),
                ('dateend', models.DateField(blank=True, default=None, null=True, verbose_name='Дата конца цели')),
                ('username', models.CharField(default=None, max_length=250, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Цель',
                'verbose_name_plural': 'Цели',
            },
        ),
    ]
