# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-10 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181210_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carts.Cart'),
        ),
    ]
