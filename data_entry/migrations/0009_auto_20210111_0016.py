# Generated by Django 3.1.2 on 2021-01-11 06:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0008_auto_20210111_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='personnel',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
    ]
