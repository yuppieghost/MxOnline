# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-26 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180726_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='fav_numx',
            new_name='fav_nums',
        ),
    ]