# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wooey', '0005_size_bytes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='script_group',
            field=models.ForeignKey(blank=True, to='wooey.ScriptGroup', null=True, on_delete=models.PROTECT),
        ),
    ]
