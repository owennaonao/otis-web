# Generated by Django 4.0.8 on 2022-12-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0022_alter_job_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='payment_preference',
            field=models.CharField(blank=True, choices=[('', 'Not specified'), ('INV', 'Invoice credits'), ('PB', 'Pro bono'), ('PPL', 'PayPal'), ('VNM', 'Venmo'), ('ZLL', 'Zelle')], default='', max_length=3),
        ),
    ]
