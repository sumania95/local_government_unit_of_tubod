# Generated by Django 3.0.3 on 2020-11-21 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_201_service_records', '0003_auto_20201121_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_record',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='service_record',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
