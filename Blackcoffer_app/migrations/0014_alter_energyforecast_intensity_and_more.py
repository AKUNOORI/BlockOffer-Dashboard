# Generated by Django 5.0.6 on 2024-05-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blackcoffer_app', '0013_alter_energyforecast_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyforecast',
            name='intensity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='energyforecast',
            name='likelihood',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='energyforecast',
            name='relevance',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='energyforecast',
            name='start_year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
