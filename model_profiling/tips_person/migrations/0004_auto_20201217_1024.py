# Generated by Django 3.0.3 on 2020-12-17 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tips_person', '0003_auto_20201216_0820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tips_person',
            options={'ordering': ['surname', 'firstname', 'middlename']},
        ),
    ]
