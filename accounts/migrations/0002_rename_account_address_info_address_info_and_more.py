# Generated by Django 4.1.6 on 2023-02-13 07:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='account_address_info',
            new_name='address_info',
        ),
        migrations.RenameModel(
            old_name='account_details',
            new_name='details',
        ),
        migrations.RenameModel(
            old_name='account_type',
            new_name='types',
        ),
    ]