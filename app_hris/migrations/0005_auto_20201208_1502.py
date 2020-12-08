# Generated by Django 3.0.3 on 2020-12-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hris', '0004_auto_20201208_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='hr_name',
            field=models.CharField(default='Adonis G. Cuevas', max_length=200),
        ),
        migrations.AddField(
            model_name='settings',
            name='hr_title',
            field=models.CharField(default='Human Resources Management Officer', max_length=200),
        ),
        migrations.AddField(
            model_name='settings',
            name='mayor_name',
            field=models.CharField(default='Richelle B. Romarate, MSCE', max_length=200),
        ),
    ]
