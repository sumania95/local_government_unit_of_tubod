# Generated by Django 3.0.3 on 2020-11-11 09:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_info_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=datetime.datetime(2020, 11, 11, 9, 0, 33, 716808))),
                ('date_to', models.DateField(default=datetime.datetime(2020, 11, 11, 9, 0, 33, 716808))),
                ('position_title', models.CharField(max_length=200)),
                ('department_office', models.CharField(max_length=200)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('pay_grade', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('is_governtment_service', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Voluntary_Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(blank=True, max_length=200)),
                ('date_from', models.DateField(default=datetime.datetime(2020, 11, 11, 9, 0, 33, 717803))),
                ('date_to', models.DateField(default=datetime.datetime(2020, 11, 11, 9, 0, 33, 717803))),
                ('no_hrs', models.IntegerField(default=0)),
                ('nature_of_work', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='References3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('tel_no', models.CharField(max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='References2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('tel_no', models.CharField(max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='References1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('tel_no', models.CharField(max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Q40',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.BooleanField(default=False)),
                ('detail_1', models.CharField(blank=True, max_length=30)),
                ('question_2', models.BooleanField(default=False)),
                ('detail_2', models.CharField(blank=True, max_length=30)),
                ('question_3', models.BooleanField(default=False)),
                ('detail_3', models.CharField(blank=True, max_length=30)),
                ('question_4', models.BooleanField(default=False)),
                ('detail_4', models.CharField(blank=True, max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Q39',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.BooleanField(default=False)),
                ('detail_1', models.CharField(blank=True, max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Q38',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.BooleanField(default=False)),
                ('detail_1', models.CharField(blank=True, max_length=30)),
                ('question_2', models.BooleanField(default=False)),
                ('detail_2', models.CharField(blank=True, max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Q37',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.BooleanField(default=False)),
                ('detail_1', models.CharField(blank=True, max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Q36',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.BooleanField(default=False)),
                ('detail_1', models.CharField(blank=True, max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Q35',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.BooleanField(default=False)),
                ('detail_1', models.CharField(blank=True, max_length=30)),
                ('question_2', models.BooleanField(default=False)),
                ('detail_2', models.CharField(blank=True, max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Q34',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.BooleanField(default=False)),
                ('detail_1', models.CharField(blank=True, max_length=30)),
                ('question_2', models.BooleanField(default=False)),
                ('detail_2', models.CharField(blank=True, max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Non_Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Member_Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Learning_Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('date_from', models.DateField(default=datetime.datetime(2020, 11, 11, 9, 0, 33, 697859))),
                ('date_to', models.DateField(default=datetime.datetime(2020, 11, 11, 9, 0, 33, 697859))),
                ('no_hrs', models.IntegerField(default=8)),
                ('type_of_ld', models.CharField(choices=[('Managerial', 'Managerial'), ('Supervisory', 'Supervisory'), ('Technical', 'Technical')], max_length=100)),
                ('sponsored_by', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Government_Other_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_id', models.CharField(max_length=30)),
                ('id_no', models.CharField(max_length=30)),
                ('date_issued', models.CharField(max_length=30)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Family_Background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spousesurname', models.CharField(blank=True, max_length=200)),
                ('spousefirstname', models.CharField(blank=True, max_length=200)),
                ('spousemiddlename', models.CharField(blank=True, max_length=200)),
                ('spouseextname', models.CharField(blank=True, max_length=200)),
                ('spouseoccupation', models.CharField(blank=True, max_length=200)),
                ('spouseemployer', models.CharField(blank=True, max_length=200)),
                ('spouseemployeraddress', models.CharField(blank=True, max_length=200)),
                ('spousetelephone', models.CharField(blank=True, max_length=200)),
                ('spouse_government_issued_id', models.CharField(blank=True, max_length=200)),
                ('spouse_government_id_no', models.CharField(blank=True, max_length=200)),
                ('spouse_government_date_issued', models.DateField(blank=True, null=True)),
                ('fathersurname', models.CharField(blank=True, max_length=200)),
                ('fatherfirstname', models.CharField(blank=True, max_length=200)),
                ('fathermiddlename', models.CharField(blank=True, max_length=200)),
                ('fatherextname', models.CharField(blank=True, max_length=200)),
                ('mothersurname', models.CharField(blank=True, max_length=200)),
                ('motherfirstname', models.CharField(blank=True, max_length=200)),
                ('mothermiddlename', models.CharField(blank=True, max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Eligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_service', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('date_of_examination', models.CharField(blank=True, max_length=200, null=True)),
                ('place_of_examination', models.CharField(blank=True, max_length=200)),
                ('examinee_number', models.IntegerField(default=0)),
                ('date_of_validity', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Educational_Background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('1', 'Elementary'), ('2', 'Secondary'), ('3', 'Vocational / Trade Course'), ('4', 'College'), ('5', 'Graduate Studies')], max_length=100)),
                ('school_name', models.CharField(blank=True, max_length=200)),
                ('course', models.CharField(blank=True, max_length=200)),
                ('period_from', models.IntegerField(default=2020)),
                ('period_to', models.IntegerField(default=2020)),
                ('units_earned', models.IntegerField(default=0)),
                ('year_graduated', models.IntegerField(default=2020)),
                ('academic_received', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('middlename', models.CharField(blank=True, max_length=200)),
                ('extname', models.CharField(blank=True, max_length=200)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2020, 11, 11, 9, 0, 33, 714816))),
                ('civil_status', models.CharField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'Widowed'), ('4', 'Separated'), ('5', 'Annulled')], max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info_profile.Profile')),
            ],
        ),
    ]
