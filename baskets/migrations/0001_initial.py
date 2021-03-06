# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baskets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('picture', models.FileField(upload_to='uploads')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
    ]
