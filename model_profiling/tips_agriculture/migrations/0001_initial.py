# Generated by Django 3.0.3 on 2020-12-27 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tips_address', '0003_auto_20201216_0820'),
        ('tips_person', '0006_tips_farmer_tips_farmerworker_tips_fisherfolk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tips_Land_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownership_document', models.CharField(choices=[('1', 'Certificate of Land Transfer'), ('2', 'Emancipation Patent'), ('3', 'Individual Certificate of Land Ownership Award (CLOA)'), ('4', 'Collective CLOA'), ('5', 'Co-ownership CLOA'), ('6', 'Agricultural sales patent'), ('7', 'Homestead patent'), ('8', 'Free Patent'), ('9', 'Certificate of Title or Regular Title'), ('10', 'Certificate of Ancestoral Domain Title'), ('11', 'Certificate of Ancestoral Land Title'), ('12', 'Tax Declaration')], max_length=200)),
                ('size', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('status', models.CharField(choices=[('1', 'Registered Owner'), ('2', 'Tenent'), ('3', 'Lessee')], max_length=200)),
                ('specify', models.CharField(blank=True, max_length=200)),
                ('commodity', models.CharField(choices=[('1', 'Rice'), ('2', 'Corn'), ('3', 'HVC'), ('4', 'Livestock'), ('5', 'Poultry'), ('6', 'Agri-fishery')], max_length=200)),
                ('farm_type', models.CharField(blank=True, choices=[('1', 'Irrigated'), ('2', 'Rainfed Upland'), ('3', 'Rainfed Lowland')], max_length=200)),
                ('is_organic', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('barangay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tips_address.Tips_Barangay')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tips_person.Tips_Person')),
            ],
        ),
        migrations.CreateModel(
            name='Tips_Livestock_Poultry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specify', models.CharField(max_length=200)),
                ('no_of_heads', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('land_parcel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tips_agriculture.Tips_Land_Description')),
            ],
        ),
    ]
