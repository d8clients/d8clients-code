# Generated by Django 4.0.2 on 2022-03-14 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_alter_workday_date_alter_workday_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='end',
            field=models.TimeField(default=datetime.time(21, 22, 13, 131911)),
        ),
        migrations.AlterField(
            model_name='workday',
            name='start',
            field=models.TimeField(default=datetime.time(21, 22, 13, 131911)),
        ),
    ]
