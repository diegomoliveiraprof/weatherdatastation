from django.contrib import admin
from .models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = (
        'hora',
        'dht22_temp',
        'dht22_umid',
        'mq2',
        'bme280_temp',
        'bme280_press',
        'gy30_lux',
        'gy30_class_lux',
        'uv_gyml8511_uv',
        'mq137_ppm_media',
        'pluvio_mm',
        'anemo_vel_ms',
        'anemo_direcao',
    )
    search_fields = ('hora',)
    list_filter = ('hora',)
