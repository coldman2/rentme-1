# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20170130_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='photo_id',
            new_name='photo',
        ),
    ]
