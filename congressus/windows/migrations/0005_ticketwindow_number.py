# Generated by Django 2.0.6 on 2018-11-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0004_ticketwindow_singlerow_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketwindow',
            name='number',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='number'),
        ),
    ]
