# Generated by Django 3.0.3 on 2020-10-22 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_info_profile', '0003_profile_url_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='url_unique',
        ),
    ]
