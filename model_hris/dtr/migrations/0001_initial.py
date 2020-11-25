# Generated by Django 3.0.3 on 2020-11-24 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dtr_Assign',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Dtr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('status', models.CharField(max_length=1000)),
                ('punch', models.CharField(max_length=1000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtr.Dtr_Assign')),
            ],
        ),
    ]