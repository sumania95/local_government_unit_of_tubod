# Generated by Django 3.0.3 on 2020-11-27 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semister', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='rating_accomplishment',
            name='semister',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='performance_management.Semister'),
            preserve_default=False,
        ),
    ]
