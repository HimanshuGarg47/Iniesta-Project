# Generated by Django 4.0.4 on 2022-05-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_employee_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]