from django.contrib import admin
from django.urls import path
from WDS.views import WeatherDataList, WeatherDataUpload
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/weather/', WeatherDataList.as_view(), name='weather-list'),
    path('api/upload/', WeatherDataUpload.as_view(), name='weather-upload'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema')),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
