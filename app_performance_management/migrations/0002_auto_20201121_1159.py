# Generated by Django 3.0.3 on 2020-11-21 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_info_profile', '0004_auto_20201121_1156'),
        ('app_performance_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_function_output', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Success_Indicator',
        ),
    ]
