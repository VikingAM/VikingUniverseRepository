# Generated by Django 4.1.6 on 2023-08-15 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_credit_score_sessionid'),
        ('tickets', '0027_remove_issue_userid_issue_useraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue_comment',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.details'),
        ),
        migrations.AlterField(
            model_name='issue_responders',
            name='responder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.details'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.details'),
        ),
        migrations.AlterField(
            model_name='task_comment',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.details'),
        ),
        migrations.AlterField(
            model_name='task_responders',
            name='responder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.details'),
        ),
    ]