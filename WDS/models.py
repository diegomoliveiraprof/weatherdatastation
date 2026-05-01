from django.db import models

class WeatherData(models.Model):
    hora = models.DateTimeField()  # convertido de yymmddHHMM para timestamp real

    dht22_temp = models.FloatField(null=True, blank=True)
    dht22_umid = models.FloatField(null=True, blank=True)
    dht22_ind_calor = models.FloatField(null=True, blank=True)

    mq2 = models.FloatField(null=True, blank=True)

    bme280_temp = models.FloatField(null=True, blank=True)
    bme280_umi = models.FloatField(null=True, blank=True)
    bme280_press = models.FloatField(null=True, blank=True)
    bme280_alti = models.FloatField(null=True, blank=True)

    gy30_lux = models.FloatField(null=True, blank=True)
    gy30_class_lux = models.CharField(max_length=50, null=True, blank=True)  # string

    uv_gyml8511_uv = models.FloatField(null=True, blank=True)
    uv_gyml8511_tensao = models.FloatField(null=True, blank=True)
    uv_gyml8511_saida = models.FloatField(null=True, blank=True)

    mq137_ppm_media = models.FloatField(null=True, blank=True)
    mq137_ppm_instant = models.FloatField(null=True, blank=True)

    uvcjmcu_indiuv = models.FloatField(null=True, blank=True)

    mq3 = models.FloatField(null=True, blank=True)
    mq4 = models.FloatField(null=True, blank=True)
    mq7 = models.FloatField(null=True, blank=True)

    pluvio_mm = models.FloatField(null=True, blank=True)

    anemo_vel_ms = models.FloatField(null=True, blank=True)
    anemo_vel_kmh = models.FloatField(null=True, blank=True)
    anemo_grau = models.FloatField(null=True, blank=True)
    anemo_direcao = models.CharField(max_length=50, null=True, blank=True)  # string

    def __str__(self):
        return f"{self.hora} - {self.dht22_temp}°C"
