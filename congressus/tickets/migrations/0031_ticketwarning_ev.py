# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20160513_1024'),
        ('tickets', '0030_auto_20160518_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketwarning',
            name='ev',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='warnings', to='events.Event'),
            preserve_default=False,
        ),
    ]