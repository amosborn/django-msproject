# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-13 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0008_auto_20200813_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='winning_bidder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
