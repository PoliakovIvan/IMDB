# Generated by Django 4.2 on 2023-06-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmspage', '0006_alter_film_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='trailer',
            field=models.URLField(default='https://www.youtube.com/'),
            preserve_default=False,
        ),
    ]
