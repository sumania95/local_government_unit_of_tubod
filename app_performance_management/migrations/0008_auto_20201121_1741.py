# Generated by Django 3.0.3 on 2020-11-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_performance_management', '0007_auto_20201121_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='ratings',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]
