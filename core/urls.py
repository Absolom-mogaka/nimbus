from django.urls import path
from .views import welcome

urlpatterns = [
    path('welcome/', welcome),
]

from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.weather_view, name='weather'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.weather_view, name='weather'),
    path('favorites/', views.favorite_cities_list, name='favorite_cities_list'),
    path('favorites/<int:pk>/', views.favorite_city_detail, name='favorite_city_detail'),
    path('', views.home_view, name='home'),
]
