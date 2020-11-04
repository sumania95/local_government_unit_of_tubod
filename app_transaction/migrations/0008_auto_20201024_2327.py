# Generated by Django 3.0.3 on 2020-10-24 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_transaction', '0007_auto_20201024_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch_generated_transaction',
            name='days',
        ),
        migrations.RemoveField(
            model_name='batch_generated_transaction',
            name='leave_type',
        ),
        migrations.AddField(
            model_name='generated_transaction',
            name='is_batch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='generated_transaction',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
