# Generated by Django 2.1 on 2020-10-16 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('middlename', models.CharField(blank=True, max_length=200)),
                ('ext_name', models.CharField(blank=True, max_length=200)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=10)),
                ('civil_status', models.CharField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'Widowed'), ('4', 'Separated'), ('5', 'Annulled')], max_length=10)),
                ('height', models.CharField(blank=True, max_length=200)),
                ('weight', models.CharField(blank=True, max_length=200)),
                ('blood_type', models.CharField(blank=True, max_length=200)),
                ('gsis', models.CharField(blank=True, max_length=200)),
                ('pagibig', models.CharField(blank=True, max_length=200)),
                ('philhealth', models.CharField(blank=True, max_length=200)),
                ('sss', models.CharField(blank=True, max_length=200)),
                ('tin', models.CharField(blank=True, max_length=200)),
                ('agency_no', models.CharField(blank=True, max_length=200)),
                ('citizenship', models.CharField(max_length=200)),
                ('residential_address', models.CharField(blank=True, max_length=200)),
                ('zipcode_1', models.CharField(blank=True, max_length=200)),
                ('permanent_address', models.CharField(blank=True, max_length=200)),
                ('zipcode_2', models.CharField(blank=True, max_length=200)),
                ('telephone', models.CharField(blank=True, max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(default='images/defaultuserprofile.png', upload_to='images/')),
                ('sl', models.DecimalField(decimal_places=3, default=0, max_digits=50)),
                ('vl', models.DecimalField(decimal_places=3, default=0, max_digits=50)),
                ('overtime', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('is_active', models.BooleanField(default=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['surname', 'firstname', 'middlename'],
            },
        ),
    ]