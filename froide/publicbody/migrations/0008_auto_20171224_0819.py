# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-24 07:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicbody', '0007_auto_20171224_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicbody',
            name='classification_name',
        ),
        migrations.RemoveField(
            model_name='publicbody',
            name='classification_slug',
        ),
    ]