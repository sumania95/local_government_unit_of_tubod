# Generated by Django 3.0.3 on 2020-12-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deducted_transaction',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Approved'), ('3', 'Disapproved')], default=1, max_length=50),
        ),
    ]
