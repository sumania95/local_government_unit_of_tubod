# Generated by Django 3.0.3 on 2020-12-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips_person', '0002_tips_address_purok_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tips_person',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
