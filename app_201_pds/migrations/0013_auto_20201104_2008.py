# Generated by Django 3.0.3 on 2020-11-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_201_pds', '0012_voluntary_work_work_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_experience',
            name='department_office',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='pay_grade',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='position_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='status',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Other_Information',
        ),
    ]