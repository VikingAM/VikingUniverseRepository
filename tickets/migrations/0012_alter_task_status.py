# Generated by Django 4.1.6 on 2023-05-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_alter_task_urgency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=250, null=True),
        ),
    ]