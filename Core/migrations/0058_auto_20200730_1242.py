# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-07-30 07:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0057_auto_20200417_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='email',
            new_name='college_email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='github_username',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='hosteler',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='year',
        ),
        migrations.AddField(
            model_name='registration',
            name='domain',
            field=models.CharField(choices=[('Developer', 'Developer'), ('Designer', 'Designer'), ('Both', 'Both')], default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='skills',
            field=models.CharField(default=datetime.date(2020, 7, 30), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='whatsapp_no',
            field=models.CharField(default=datetime.date(2020, 7, 30), max_length=10),
            preserve_default=False,
        ),
    ]
