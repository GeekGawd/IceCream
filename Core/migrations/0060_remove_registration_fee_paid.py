# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-07-31 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0059_registration_other_handles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='fee_paid',
        ),
    ]
