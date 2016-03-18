# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-17 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0001_Initialize Task Table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='toDo.User'),
            preserve_default=False,
        ),
    ]
