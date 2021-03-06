# Generated by Django 3.0.3 on 2020-12-22 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tips_person', '0005_tips_person_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tips_Fisherfolk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_fish_capture', models.BooleanField(default=False)),
                ('is_aquaculture', models.BooleanField(default=False)),
                ('is_gleaning', models.BooleanField(default=False)),
                ('is_fish_processing', models.BooleanField(default=False)),
                ('is_fish_vending', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tips_person.Tips_Person')),
            ],
        ),
        migrations.CreateModel(
            name='Tips_Farmerworker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_land_preparation', models.BooleanField(default=False)),
                ('is_planting_or_transplanting', models.BooleanField(default=False)),
                ('is_cultivation', models.BooleanField(default=False)),
                ('is_harvesting', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tips_person.Tips_Person')),
            ],
        ),
        migrations.CreateModel(
            name='Tips_Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rice', models.BooleanField(default=False)),
                ('is_corn', models.BooleanField(default=False)),
                ('other_crops', models.CharField(blank=True, max_length=200)),
                ('livestock', models.CharField(blank=True, max_length=200)),
                ('poultry', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tips_person.Tips_Person')),
            ],
        ),
    ]
