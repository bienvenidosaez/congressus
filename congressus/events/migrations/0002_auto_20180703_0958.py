# Generated by Django 2.0.6 on 2018-07-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketfield',
            name='label',
            field=models.TextField(verbose_name='label'),
        ),
        migrations.AlterField(
            model_name='ticketfield',
            name='type',
            field=models.CharField(choices=[('email', 'Email'), ('tel', 'Phone'), ('url', 'URL'), ('text', 'Text'), ('textarea', 'TextArea'), ('check', 'CheckBox'), ('select', 'Select'), ('html', 'HTML')], default='text', max_length=100, verbose_name='type'),
        ),
    ]