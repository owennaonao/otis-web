# Generated by Django 4.0.8 on 2022-12-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_alter_job_spades_bounty_alter_job_usd_bounty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, help_text='A job description of what you should do'),
        ),
    ]