# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 14:25
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wooey', '0022_add_collapse_arguments'),
    ]

    operations = [
        migrations.AddField(
            model_name='scriptparameter',
            name='script_versions',
            field=models.ManyToManyField(related_name='scriptparameters', to='wooey.ScriptVersion'),
        ),
        migrations.AlterField(
            model_name='scriptparameter',
            name='script_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scriptparameter', to='wooey.ScriptVersion'),
        ),
    ]
