# Generated by Django 3.0.3 on 2020-10-24 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_transaction', '0004_auto_20201024_1703'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rejected_Log',
            new_name='Rejected_Transaction',
        ),
        migrations.AlterField(
            model_name='rejected_transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
