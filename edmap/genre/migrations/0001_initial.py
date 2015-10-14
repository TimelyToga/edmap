# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('key', models.CharField(max_length=256, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('key', models.CharField(max_length=256, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('description', models.CharField(max_length=512)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('key', models.CharField(max_length=256, serialize=False, auto_created=True, primary_key=True)),
                ('influencee', models.ForeignKey(to='genre.Genre')),
                ('influencer', models.ForeignKey(related_name='+', to='genre.Genre')),
            ],
            options={
                'ordering': ('influencer',),
            },
        ),
        migrations.AddField(
            model_name='example',
            name='owner',
            field=models.ForeignKey(to='genre.Genre'),
        ),
    ]
