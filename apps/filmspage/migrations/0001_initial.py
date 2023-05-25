# Generated by Django 4.2 on 2023-05-22 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=255, verbose_name='movie')),
                ('date', models.DateField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('genre', models.CharField(max_length=255, verbose_name='genre')),
                ('photo', models.BinaryField()),
            ],
        ),
    ]
