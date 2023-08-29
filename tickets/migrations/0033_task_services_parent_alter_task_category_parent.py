# Generated by Django 4.1.6 on 2023-08-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0032_task_comment_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_services',
            name='parent',
            field=models.CharField(blank=True, default=0, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='task_category',
            name='parent',
            field=models.CharField(blank=True, default=0, max_length=250, null=True),
        ),
    ]