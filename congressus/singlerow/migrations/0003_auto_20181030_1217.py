# Generated by Django 2.0.6 on 2018-10-30 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_ticketfield_show_in_tws'),
        ('singlerow', '0002_auto_20180811_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleRowConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_text', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_row_config', to='events.Event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'Single Row Config',
            },
        ),
        migrations.AlterModelOptions(
            name='singlerowtail',
            options={'ordering': ['date'], 'verbose_name': 'Single Row Tail'},
        ),
    ]
