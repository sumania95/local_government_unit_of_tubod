# Generated by Django 3.0.3 on 2020-12-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educational_background',
            name='units_earned',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]