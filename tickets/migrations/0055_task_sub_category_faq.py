# Generated by Django 4.1.6 on 2023-09-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0054_task_services_sub_type_introduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_sub_category',
            name='faq',
            field=models.BooleanField(default=0),
        ),
    ]