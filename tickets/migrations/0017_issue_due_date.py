# Generated by Django 4.1.6 on 2023-07-13 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0016_alter_issue_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
