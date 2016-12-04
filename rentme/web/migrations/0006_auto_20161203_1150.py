# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20161203_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='id',
            new_name='listrict_id',
        ),
        migrations.RenameField(
            model_name='locality',
            old_name='id',
            new_name='locality_id',
        ),
        migrations.RenameField(
            model_name='membershipdistrict',
            old_name='id',
            new_name='district_id',
        ),
        migrations.RenameField(
            model_name='membershiplocality',
            old_name='id',
            new_name='locality_id',
        ),
        migrations.RenameField(
            model_name='suburb',
            old_name='id',
            new_name='suburb_id',
        ),
    ]