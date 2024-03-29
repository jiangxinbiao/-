# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-06-11 07:47
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminIMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=200, null=True, verbose_name='文件名')),
                ('img', models.ImageField(upload_to='./admin')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16, null=True, verbose_name='昵称')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('body', models.TextField(blank=True, null=True, verbose_name='评论正文')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='作品标签')),
                ('updatetime', models.DateField(auto_now=True, verbose_name='修改时间')),
                ('createtime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '作品标签',
                'verbose_name_plural': '作品标签',
                'db_table': 'Label',
                'ordering': ['-updatetime'],
            },
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='作品名称')),
                ('photo', models.ImageField(height_field='url_height', upload_to='avatar', verbose_name='作品', width_field='url_width')),
                ('url_height', models.PositiveIntegerField(blank=True, null=True, verbose_name='图片宽')),
                ('url_width', models.PositiveIntegerField(blank=True, null=True, verbose_name='图片长')),
                ('Ph', models.IntegerField(blank=True, null=True, verbose_name='作品长')),
                ('Pt', models.IntegerField(blank=True, null=True, verbose_name='作品宽')),
                ('Cname', models.CharField(blank=True, max_length=50, null=True, verbose_name='作者名')),
                ('Createtime', models.DateField(auto_now_add=True, null=True, verbose_name='创作时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('text', DjangoUeditor.models.UEditorField(blank=True, null=True, verbose_name='作品说明')),
            ],
            options={
                'verbose_name': '作品',
                'verbose_name_plural': '作品',
                'db_table': 'painting',
                'ordering': ['-updated'],
            },
        ),
    ]
