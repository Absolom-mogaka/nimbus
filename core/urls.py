from django.urls import path
from . import views, auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('weather/<str:city>/', views.weather_view, name='weather'),
    path('favorites/', views.favorite_cities_list, name='favorite_cities_list'),
    path('favorites/<int:pk>/', views.favorite_city_detail, name='favorite_city_detail'),

    # Auth endpoints
    path('auth/register/', auth_views.register_user, name='register_user'),
    path('auth/login/', auth_views.get_tokens_for_user, name='login_user'),
]
