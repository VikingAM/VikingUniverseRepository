# Generated by Django 4.1.6 on 2023-08-15 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0029_rename_owner_task_owner_accountdetails_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='owner_accountDetails',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
    ]
