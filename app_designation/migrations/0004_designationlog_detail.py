# Generated by Django 3.0.3 on 2020-11-04 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_designation', '0003_remove_plantilla_is_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='designationlog',
            name='detail',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]