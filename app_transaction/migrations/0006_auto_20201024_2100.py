# Generated by Django 3.0.3 on 2020-10-24 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0005_auto_20201024_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rejected_transaction',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='rejected_transaction',
            name='date_to',
        ),
    ]