# Generated by Django 4.0.2 on 2022-03-14 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_assignment_confirmed_alter_assignment_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 15)),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start',
            field=models.TimeField(default=datetime.time(1, 18, 59, 757126)),
        ),
    ]
