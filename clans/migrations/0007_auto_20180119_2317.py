# Generated by Django 2.0 on 2018-01-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0006_auto_20171221_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]