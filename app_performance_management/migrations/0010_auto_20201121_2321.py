# Generated by Django 3.0.3 on 2020-11-21 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_performance_management', '0009_auto_20201121_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='accomplishment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_performance_management.Accomplishment'),
        ),
    ]
