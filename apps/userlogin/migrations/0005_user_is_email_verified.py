# Generated by Django 4.2 on 2023-06-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0004_remove_user_firstname_remove_user_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]