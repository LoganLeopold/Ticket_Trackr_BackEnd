# Generated by Django 2.1.7 on 2019-11-28 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_trackr_app', '0004_auto_20190904_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airportmodel',
            name='delayIndexUrl',
        ),
    ]
