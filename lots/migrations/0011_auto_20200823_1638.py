# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-23 16:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0010_auto_20200823_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='winning_bidder',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
