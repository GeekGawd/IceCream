# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-02-06 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0049_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=5),
        ),
    ]
