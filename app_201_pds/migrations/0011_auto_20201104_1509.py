# Generated by Django 3.0.3 on 2020-11-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_201_pds', '0010_eligibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eligibility',
            name='date_of_examination',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='date_of_validity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]