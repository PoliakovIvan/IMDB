# Generated by Django 4.2 on 2023-06-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenresList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=255, verbose_name='genres')),
            ],
        ),
    ]
