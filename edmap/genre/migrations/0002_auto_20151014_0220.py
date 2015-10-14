# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='key',
            field=models.IntegerField(serialize=False, auto_created=True, primary_key=True),
        ),
    ]
