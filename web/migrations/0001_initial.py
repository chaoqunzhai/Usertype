# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='用户名称')),
                ('token', models.CharField(db_index=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True, verbose_name=' 提交故障')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User', to_field='username')),
            ],
        ),
    ]