# Generated by Django 3.0.3 on 2021-01-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20201227_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deducted_transaction',
            name='leave_type',
            field=models.CharField(choices=[('1', 'Sick Leave'), ('2', 'Vacation Leave'), ('3', 'Special Leave'), ('4', 'Offset'), ('5', 'Maternity Leave'), ('6', 'Faternity Leave')], max_length=50),
        ),
        migrations.AlterField(
            model_name='generated_transaction',
            name='leave_type',
            field=models.CharField(choices=[('1', 'Sick Leave'), ('2', 'Vacation Leave'), ('3', 'Special Leave'), ('4', 'Offset'), ('5', 'Maternity Leave'), ('6', 'Faternity Leave')], max_length=50),
        ),
    ]
