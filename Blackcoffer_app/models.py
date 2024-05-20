from django.db import models
import os

class EnergyForecast(models.Model):
    end_year = models.CharField(max_length=200, blank=True, null=True)
    # end_year = models.IntegerField(blank=True, null=True)
    intensity = models.CharField(max_length=200, blank=True, null=True)
    # intensity = models.IntegerField(blank=True, null=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    topic = models.CharField(max_length=200, blank=True, null=True)
    insight = models.CharField(max_length=1000, blank=True, null=True)
    url = models.URLField(max_length=1000)
    region = models.CharField(max_length=200, blank=True, null=True)
    # start_year = models.IntegerField(blank=True, null=True)
    start_year = models.CharField(max_length=200, blank=True, null=True)
    impact = models.CharField(max_length=200, blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    relevance = models.CharField(max_length=200, blank=True, null=True)
    # relevance = models.IntegerField(blank=True, null=True)
    pestle = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    # likelihood = models.IntegerField(blank=True, null=True)
    likelihood = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


def unique_json_file_path(instance, filename):
    file_path = os.path.join('json_files', filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)
    
    return file_path

class JsonFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=unique_json_file_path)
