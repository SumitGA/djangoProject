# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_logo',
            new_name='album_log',
        ),
    ]
