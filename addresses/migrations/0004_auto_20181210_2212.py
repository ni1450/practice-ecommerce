# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-10 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_auto_20181210_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='billing_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='billing.BillingProfile'),
        ),
    ]
