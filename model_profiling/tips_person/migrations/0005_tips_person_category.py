# Generated by Django 3.0.3 on 2020-12-21 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tips_person', '0004_auto_20201217_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tips_Person_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnsp', models.BooleanField(default=False)),
                ('ynsp', models.BooleanField(default=False)),
                ('wedc', models.BooleanField(default=False)),
                ('pwd', models.BooleanField(default=False)),
                ('fhona', models.BooleanField(default=False)),
                ('solo_parent', models.BooleanField(default=False)),
                ('ip', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tips_person.Tips_Person')),
            ],
        ),
    ]
