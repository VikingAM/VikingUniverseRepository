# Generated by Django 4.1.6 on 2023-06-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0014_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='ticket_status',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]