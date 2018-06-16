# Generated by Django 2.0.6 on 2018-06-16 19:44

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketWindow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('code', models.CharField(help_text='code to show in tickets', max_length=5, verbose_name='code')),
                ('cash', models.FloatField(default=0, verbose_name='cash in the ticket window')),
                ('location', models.CharField(blank=True, max_length=500, null=True, verbose_name='location')),
                ('online', models.BooleanField(default=False, verbose_name='online')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='windows', to='events.Event', verbose_name='event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'ticket window',
                'verbose_name_plural': 'ticket windows',
                'ordering': ['-event', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TicketWindowCashMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('change', 'Change'), ('preturn', 'Parcial return'), ('return', 'Final return')], default='change', max_length=10, verbose_name='type')),
                ('amount', models.FloatField(default=0, verbose_name='amount')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('window', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='windows.TicketWindow', verbose_name='window')),
            ],
            options={
                'verbose_name': 'ticket window cash movement',
                'verbose_name_plural': 'ticket window cash movements',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TicketWindowSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='price')),
                ('payed', models.FloatField(default=0, verbose_name='payed')),
                ('change', models.FloatField(default=0, verbose_name='change')),
                ('payment', models.CharField(choices=[('cash', 'Cash'), ('card', 'Credit Card')], default='cash', max_length=10, verbose_name='payment')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='tickets.MultiPurchase', verbose_name='multipurchase')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('window', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='windows.TicketWindow', verbose_name='window')),
            ],
            options={
                'verbose_name': 'ticket window sale',
                'verbose_name_plural': 'ticket window sales',
            },
        ),
    ]
