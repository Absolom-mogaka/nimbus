from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def welcome(request):
    return Response({"message": "Welcome to Nimbus "})

import requests
from django.http import JsonResponse
from django.conf import settings

def weather_view(request, city):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return JsonResponse(result)
    else:
        return JsonResponse({"error": "City not found"}, status=404)
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FavoriteCity
from .serializers import FavoriteCitySerializer

@api_view(['GET', 'POST'])
def favorite_cities_list(request):
    if request.method == 'GET':
        cities = FavoriteCity.objects.all().order_by('-created_at')
        serializer = FavoriteCitySerializer(cities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FavoriteCitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def favorite_city_detail(request, pk):
    try:
        city = FavoriteCity.objects.get(pk=pk)
    except FavoriteCity.DoesNotExist:
        return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavoriteCitySerializer(city)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FavoriteCitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
