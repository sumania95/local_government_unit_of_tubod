# Generated by Django 3.0.3 on 2020-11-04 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_201_pds', '0014_delete_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learning_development',
            old_name='fromdate',
            new_name='date_from',
        ),
        migrations.RenameField(
            model_name='learning_development',
            old_name='todate',
            new_name='date_to',
        ),
        migrations.RenameField(
            model_name='learning_development',
            old_name='nohrs',
            new_name='no_hrs',
        ),
        migrations.RenameField(
            model_name='learning_development',
            old_name='sponsoredby',
            new_name='sponsored_by',
        ),
        migrations.RenameField(
            model_name='learning_development',
            old_name='typeofld',
            new_name='type_of_ld',
        ),
    ]
