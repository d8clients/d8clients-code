# Generated by Django 4.0.2 on 2022-03-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_user_business_only'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default='', max_length=64),
        ),
    ]
