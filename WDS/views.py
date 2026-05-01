import csv
from datetime import datetime
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django_filters.rest_framework import DjangoFilterBackend


def safe_float(value):
    try:
        f = float(value)
        if f != f:  # NaN check (NaN != NaN)
            return None
        return f
    except (ValueError, TypeError):
        return None

class WeatherDataList(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    permission_classes = []  # sem autenticação para GET
    # habilitar filtros
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'hora',
        'dht22_temp',
        'dht22_umid',
        'mq2',
        'bme280_temp',
        'gy30_class_lux',
        'anemo_direcao',
    ]

class WeatherDataUpload(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            hora_str = row['Hora']
            hora_dt = datetime.strptime(hora_str, "%y%m%d%H%M")

            WeatherData.objects.create(
                hora=hora_dt,
                dht22_temp=safe_float(row['DHT22(Temp)']),
                dht22_umid=safe_float(row['DHT22(Umid)']),
                dht22_ind_calor=safe_float(row['DHT22(Ind.Calor)']),
                mq2=safe_float(row['MQ2']),
                bme280_temp=safe_float(row['BME-280(Temp)']),
                bme280_umi=safe_float(row['BME-280(Umi.)']),
                bme280_press=safe_float(row['BME-280(Press.)']),
                bme280_alti=safe_float(row['BME-280(Alti.)']),
                gy30_lux=safe_float(row['GY30(Lux)']),
                gy30_class_lux=row['GY30(Class.Lux)'],  # string
                uv_gyml8511_uv=safe_float(row['UV GYML8511(UV)']),
                uv_gyml8511_tensao=safe_float(row['UV GYML8511(Tensao)']),
                uv_gyml8511_saida=safe_float(row['UV GYML8511(Saida)']),
                mq137_ppm_media=safe_float(row['MQ-137(PPM Media)']),
                mq137_ppm_instant=safe_float(row['MQ-137(PPM Instant)']),
                uvcjmcu_indiuv=safe_float(row['UVcjmcu(IndiUV)']),
                mq3=safe_float(row['MQ-3']),
                mq4=safe_float(row['MQ-4']),
                mq7=safe_float(row['MQ-7']),
                pluvio_mm=safe_float(row['Pluvio.(MM)']),
                anemo_vel_ms=safe_float(row['Anemo(Vel MS)']),
                anemo_vel_kmh=safe_float(row['Anemo(Vel KMH)']),
                anemo_grau=safe_float(row['Anemo(Grau)']),
                anemo_direcao=row['Anemo(Direcao)'],  # string
            )
        return Response({"status": "Dados inseridos com sucesso"})
