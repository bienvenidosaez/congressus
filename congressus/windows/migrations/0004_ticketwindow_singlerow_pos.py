# Generated by Django 2.0.6 on 2018-10-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windows', '0003_ticketwindow_supplement'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketwindow',
            name='singlerow_pos',
            field=models.CharField(choices=[('R', 'Right'), ('L', 'Left')], default='R', max_length=1, verbose_name='single row position'),
        ),
    ]
