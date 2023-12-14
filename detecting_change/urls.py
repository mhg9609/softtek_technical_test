from django.urls import path
from detecting_change.views import (detect_change, set_default_weathers,
                                   WeatherDetail, list_weathers)

urlpatterns = [
    # TECHNICAL TEST PATH
    path('detecting-change/', detect_change, name='detecting_change'),
    # THESE PATHS ARE NOT NECESSARY FOR THE TECHNICAL TEST.
    path('detecting-change/weathers-list/', list_weathers, name='weathers_list'),
    path('detecting-change/weather/<str:date>/', WeatherDetail.as_view(), name='weather_detail'),
    # THIS PATH WAS CREATED JUST TO ADD THE DEFAULT VALUES TO THE DATABASE FOR TEST
    path('detecting-change/default-weathers/', set_default_weathers, name='set_default_weathers'), # Just created to add data for test
]
