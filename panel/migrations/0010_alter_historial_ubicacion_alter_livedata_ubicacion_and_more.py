# Generated by Django 4.2 on 2023-04-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_alter_noregistrados_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='ubicacion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='livedata',
            name='ubicacion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='noregistrados',
            name='ubicacion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
