# Generated by Django 4.0.4 on 2022-05-24 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_employee_options_alter_employee_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee_id',
            new_name='username',
        ),
    ]
