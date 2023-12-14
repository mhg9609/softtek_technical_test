from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime
from detecting_change.models import Weather


# TECHNICAL TEST FUNCTION
@api_view(['GET'])
def detect_change(request):
    weather_data = Weather.objects.order_by('date')
    bad_weather_dates = [{'date': weather.date, 'was_rainy': weather.was_rainy} for i, weather in enumerate(weather_data) if i > 0 and weather.was_rainy and not weather_data[i-1].was_rainy]
    return Response(bad_weather_dates, status=200)
  
# THIS FUNCTION IS NOT NECESSARY FOR THE TECHNICAL TEST.
@api_view(['GET'])
def list_weathers(request):
    weathers = Weather.objects.all()
    weather_list = [{
        'date': weather.date,
        'was_rainy': weather.was_rainy
    } for weather in weathers]
    return Response(weather_list, status=200)

# THIS FUNCTION WAS CREATED JUST TO ADD THE DEFAULT VALUES TO THE DATABASE FOR TEST.
@api_view(['GET'])
def set_default_weathers(request):
    Weather.objects.all().delete()
    weathers = [
        ('2020-01-01', False),
        ('2020-01-02', True),
        ('2020-01-03', True),
        ('2020-01-04', False),
        ('2020-01-05', False),
        ('2020-01-06', True),
        ('2020-01-07', False),
        ('2020-01-08', True),
        ('2020-01-09', True),
        ('2020-01-10', True)
    ]

    for date, was_rainy in weathers:
        weather = Weather(
            date=datetime.strptime(date, '%Y-%m-%d'),
            was_rainy=was_rainy
        )
        weather.save()
    return Response({'message': 'Default weathers added.'}, status=200)

# THIS CLASS IS NOT NECESSARY FOR THE TECHNICAL TEST.
class WeatherDetail(APIView):
    def get(self, request, date):
        try:
            weather = Weather.objects.get(date=date)
            return Response({
                'date': weather.date,
                'was_rainy': weather.was_rainy
            }, status=200)
        except Weather.DoesNotExist:
            return Response({'message': 'Weather data does not exist.'}, status=404)

    def delete(self, request, date):
        try:
            weather = Weather.objects.get(date=date)
            weather.delete()
            return JsonResponse({'message': 'Weather data deleted.'}, status=200)
        except Weather.DoesNotExist:
            return JsonResponse({'message': 'Weather data does not exist.'}, status=404)

    def put(self, request, date):
        try:
            weather = Weather.objects.get(date=date)
            weather.date = request.data.get('date', weather.date)
            weather.was_rainy = request.data.get('was_rainy', weather.was_rainy)
            weather.save()
            return JsonResponse({'message': 'Weather data updated.'}, status=200)
        except Weather.DoesNotExist:
            return JsonResponse({'message': 'Weather data does not exist.'}, status=404)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def post(self, request, date):
        try:
            date = request.data.get('date')
            was_rainy = request.data.get('was_rainy')
            weather = Weather(
                date=date,
                was_rainy=was_rainy
            )
            weather.save()
            return Response({'message': 'Weather data created.'}, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)
