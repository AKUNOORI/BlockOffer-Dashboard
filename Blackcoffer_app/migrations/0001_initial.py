# Generated by Django 5.0.6 on 2024-05-15 06:18

import Blackcoffer_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('intensity', models.IntegerField()),
                ('sector', models.TextField()),
                ('topic', models.TextField()),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.TextField()),
                ('start_year', models.IntegerField(blank=True, null=True)),
                ('impact', models.TextField(blank=True)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.TextField()),
                ('relevance', models.IntegerField()),
                ('pestle', models.TextField()),
                ('source', models.TextField()),
                ('title', models.TextField()),
                ('likelihood', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JsonFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=Blackcoffer_app.models.unique_json_file_path)),
            ],
        ),
    ]
