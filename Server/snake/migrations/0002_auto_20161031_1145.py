# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 11:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='apple_B',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Blue'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='apple_G',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Green'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='apple_R',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Red'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='background_B',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Blue'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='background_G',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Green'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='background_R',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Red'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='snake_B',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Blue'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='snake_G',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Green'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='snake_R',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Red'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='walls_B',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Blue'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='walls_G',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Green'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='walls_R',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.MinValueValidator(0)], verbose_name='Red'),
        ),
    ]
