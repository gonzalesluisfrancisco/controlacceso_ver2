# Generated by Django 4.2 on 2023-04-17 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_postcardidevent_deviceid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcardidevent',
            old_name='cardid',
            new_name='cardID',
        ),
    ]
