# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_member_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bidder_and_watchers',
            field=models.IntegerField(default=0),
        ),
    ]