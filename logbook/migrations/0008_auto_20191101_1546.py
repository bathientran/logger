# Generated by Django 2.1.7 on 2019-11-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0007_auto_20191101_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endTime',
            field=models.DateTimeField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='startTime',
            field=models.DateTimeField(verbose_name='Start Date'),
        ),
    ]
