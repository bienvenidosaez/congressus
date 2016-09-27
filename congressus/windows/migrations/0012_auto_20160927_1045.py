# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-27 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0011_auto_20160920_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketwindowcashmovement',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='ticketwindowcashmovement',
            name='type',
            field=models.CharField(choices=[('change', 'Change'), ('preturn', 'Parcial return'), ('return', 'Final return')], default='change', max_length=10, verbose_name='type'),
        ),
    ]
