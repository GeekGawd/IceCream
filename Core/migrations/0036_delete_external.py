# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-28 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0035_contactinfo_external'),
    ]

    operations = [
        migrations.DeleteModel(
            name='External',
        ),
    ]
