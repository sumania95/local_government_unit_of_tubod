# Generated by Django 3.0.3 on 2020-12-21 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tips_nature_of_services', '0003_auto_20201220_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips_recommended_services',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
