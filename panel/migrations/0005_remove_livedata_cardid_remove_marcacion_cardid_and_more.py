# Generated by Django 4.2 on 2023-04-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_livedata_cardidhex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livedata',
            name='cardid',
        ),
        migrations.RemoveField(
            model_name='marcacion',
            name='cardid',
        ),
        migrations.RemoveField(
            model_name='noregistrados',
            name='cardid',
        ),
        migrations.RemoveField(
            model_name='personalregistrado',
            name='cardid',
        ),
        migrations.AddField(
            model_name='livedata',
            name='empresa',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='marcacion',
            name='cardidHex',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='marcacion',
            name='empresa',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='noregistrados',
            name='cardidHex',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='personalregistrado',
            name='cardidHex',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='personalregistrado',
            name='empresa',
            field=models.CharField(max_length=50, null=True),
        ),
    ]