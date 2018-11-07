# Generated by Django 2.0.6 on 2018-10-30 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0004_ticketwindow_singlerow_pos'),
        ('singlerow', '0005_singlerowconfig_last_window'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlerowconfig',
            name='waiting',
            field=models.ManyToManyField(related_name='config_waiting', to='windows.TicketWindow', verbose_name='waiting ticket windows'),
        ),
        migrations.AlterField(
            model_name='singlerowconfig',
            name='last_window',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='config_last', to='windows.TicketWindow', verbose_name='last ticket window'),
        ),
    ]
