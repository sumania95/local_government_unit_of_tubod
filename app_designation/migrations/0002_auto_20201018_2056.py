# Generated by Django 2.1 on 2020-10-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_designation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantilla',
            name='status',
            field=models.CharField(choices=[('1', 'Permanent'), ('2', 'Co-Terminus'), ('3', 'Elected')], max_length=100),
        ),
    ]
