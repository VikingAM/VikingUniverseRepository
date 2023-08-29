# Generated by Django 4.1.6 on 2023-08-29 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0040_issue_comment_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue_comment_file',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.issue'),
        ),
    ]
