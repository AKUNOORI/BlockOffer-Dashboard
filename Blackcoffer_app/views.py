from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import JsonUploadForm
from .models import JsonFile, EnergyForecast
import json
import csv
from datetime import datetime
import pytz
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

def ReadJson(request):
    if request.method == 'POST':
        try:
            form = JsonUploadForm(request.POST, request.FILES)
            if form.is_valid():
                json_file = form.save(commit=False)
                existing_file = JsonFile.objects.filter(file__icontains = json_file.file)
                if existing_file.exists():
                    return JsonResponse({'message': 'File already exists'})
                else:
                    json_file.save()

                ProcessJson(json_file.file.path)
                return JsonResponse({"message": "Successefully created"})
        except Exception as ex:
            return JsonResponse({"error": str(ex)})
    else:
        form = JsonUploadForm()
    return render(request, 'upload.html', {'form': form})

def ProcessJson(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

        successful_records = 0
        failed_records = []
        
        for item in data:
            try:
                end_year = item.get('end_year') if item.get('end_year') != '' else ''
                start_year = item.get('start_year') if item.get('start_year') != '' else ''
                relevance = item.get('relevance') if item.get('relevance') != '' else ''
                likelihood = item["likelihood"] if item["likelihood"] != '' else ''
                intensity = item["intensity"] if item["intensity"] != '' else ''

                added_date = datetime.strptime(item['added'], '%B, %d %Y %H:%M:%S')
                added_date = pytz.utc.localize(added_date)

                if item["published"] != "":
                    published_date = datetime.strptime(item["published"], '%B, %d %Y %H:%M:%S')
                    published_date = pytz.utc.localize(published_date)
                else:
                    published_date = None
                    
                energy_forecast_instance = EnergyForecast(end_year=end_year, intensity=intensity, sector=item.get('sector'), topic=item.get('topic'), insight=item.get('insight'), url=item.get('url'), region=item.get('region'), start_year=start_year, impact=item.get('impact'), added=added_date, published=published_date, country=item.get('country'), relevance=relevance, pestle=item.get('pestle'), source=item.get('source'), title=item.get('title'), likelihood=likelihood)
                energy_forecast_instance.save()
                successful_records += 1
            except KeyError as ex:
                failed_records.append({"KeyError": str(ex)})
            except ValueError as ex:
                failed_records.append({"ValueError": str(ex), "item": item})

        return JsonResponse({
            "message": f"{successful_records} records saved successfully.",
            "failed_records": failed_records
        })
            

@csrf_exempt
def visualization(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode('utf-8'))
            end_year = body.get('end_year')
            topic = body.get('topic')
            sector = body.get('sector')
            region = body.get('region')
            pestle = body.get('pestle')
            source = body.get('source')
            country = body.get('country')

            filters = Q()
            if end_year:
                filters &= Q(end_year=end_year)
            if topic:
                filters &= Q(topic=topic)
            if sector:
                filters &= Q(sector=sector)
            if region:
                filters &= Q(region=region)
            if pestle:
                filters &= Q(pestle=pestle)
            if source:
                filters &= Q(source=source)
            if country:
                filters &= Q(country=country)

            visualization_data = EnergyForecast.objects.filter(filters).exclude(country='').values("intensity", "likelihood", "relevance", "start_year", "country", "topic", "region")
            
            return JsonResponse({"data": list(visualization_data)}, safe=False)
        except Exception as ex:
            return JsonResponse({"error": str(ex)})