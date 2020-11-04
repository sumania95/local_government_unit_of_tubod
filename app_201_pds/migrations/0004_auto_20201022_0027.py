# Generated by Django 3.0.3 on 2020-10-21 16:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_201_service_records', '0001_initial'),
        ('app_rewards_recognitions', '0002_auto_20201021_2335'),
        ('app_info_profile', '0002_retired'),
        ('app_designation', '0002_auto_20201018_2056'),
        ('app_201_pds', '0003_reference'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FamilyBackground',
            new_name='Family_Background',
        ),
        migrations.RenameModel(
            old_name='LearningDevelopment',
            new_name='Learning_Development',
        ),
        migrations.RenameModel(
            old_name='OtherInformation',
            new_name='Other_Information',
        ),
    ]
