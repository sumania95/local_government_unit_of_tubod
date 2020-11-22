# Generated by Django 3.0.3 on 2020-11-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_internet', '0004_auto_20201122_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mikrotik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('user_profile', models.CharField(max_length=200)),
                ('user_limit_update', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
