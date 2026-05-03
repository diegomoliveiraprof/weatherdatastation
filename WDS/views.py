import csv
from datetime import datetime
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


def safe_float(value):
    """
    Converte valor para float de forma segura.
    Aceita negativos, zero e valores vazios.
    Retorna None se não for possível converter.
    """
    if value is None or str(value).strip() == "":
        return None
    try:
        f = float(value)
        if f != f:  # NaN check
            return None
        return f
    except (ValueError, TypeError):
        return None


# 🔎 Filtros personalizados
class WeatherDataFilter(django_filters.FilterSet):
    #Filtro por data (sem hora)
    data = django_filters.DateFilter(field_name="hora", lookup_expr="date", label="Data")
    #Filtro por intervalo de data
    data_range = django_filters.DateFromToRangeFilter(field_name="hora", label="Data Intervalo")
    #Filtro por hora
    hora_only = django_filters.TimeFilter(field_name="hora", lookup_expr="time", label="Horário")
    #Filtro por intervalo de temperatura
    temperatura_range = django_filters.RangeFilter(field_name="dht22_temp", label="Temp DHT22 Intervalo")
    #Filtro por intervalo de umidade
    umidade_range = django_filters.RangeFilter(field_name="dht22_umid", label="Umidade DHT22 Intervalo")
    #Filtro por intervalo de pluviometria
    pluvio_range = django_filters.RangeFilter(field_name="pluvio_mm", label="Chuva pluvio Intervalo")

    class Meta:
        model = WeatherData
        fields = [
            'data',
            'data_range',
            'hora_only',
            'temperatura_range',
            'umidade_range',
            'pluvio_range',
            'dht22_temp',
            'dht22_umid',
            'mq2',
            'bme280_temp',
            'gy30_class_lux',
            'anemo_direcao',
        ]


class WeatherDataList(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    permission_classes = []  # sem autenticação para GET
    filter_backends = [DjangoFilterBackend]
    filterset_class = WeatherDataFilter


class WeatherDataUpload(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        count = 0
        for row in reader:
            hora_str = row['Hora'].strip()
            hora_str = hora_str[:10]  # garante 10 dígitos
            hora_dt = datetime.strptime(hora_str, "%y%m%d%H%M")

            WeatherData.objects.create(
                hora=hora_dt,
                dht22_temp=safe_float(row.get('DHT22(Temp)')),
                dht22_umid=safe_float(row.get('DHT22(Umid)')),
                dht22_ind_calor=safe_float(row.get('DHT22(Ind.Calor)')),
                mq2=safe_float(row.get('MQ2')),
                bme280_temp=safe_float(row.get('BME-280(Temp)')),
                bme280_umi=safe_float(row.get('BME-280(Umi.)')),
                bme280_press=safe_float(row.get('BME-280(Press.)')),
                bme280_alti=safe_float(row.get('BME-280(Alti.)')),
                gy30_lux=safe_float(row.get('GY30(Lux)')),
                gy30_class_lux=row.get('GY30(Class.Lux)'),  # string
                uv_gyml8511_uv=safe_float(row.get('UV GYML8511(UV)')),
                uv_gyml8511_tensao=safe_float(row.get('UV GYML8511(Tensao)')),
                uv_gyml8511_saida=safe_float(row.get('UV GYML8511(Saida)')),
                mq137_ppm_media=safe_float(row.get('MQ-137(PPM Media)')),
                mq137_ppm_instant=safe_float(row.get('MQ-137(PPM Instant)')),
                uvcjmcu_indiuv=safe_float(row.get('UVcjmcu(IndiUV)')),
                mq3=safe_float(row.get('MQ-3')),
                mq4=safe_float(row.get('MQ-4')),
                mq7=safe_float(row.get('MQ-7')),
                pluvio_mm=safe_float(row.get('Pluvio.(MM)')),
                anemo_vel_ms=safe_float(row.get('Anemo(Vel MS)')),
                anemo_vel_kmh=safe_float(row.get('Anemo(Vel KMH)')),
                anemo_grau=safe_float(row.get('Anemo(Grau)')),
                anemo_direcao=row.get('Anemo(Direcao)'),  # string
            )
            count += 1

        return Response(
            {
                "status": "Upload realizado com sucesso",
                "arquivo": file.name,
                "linhas_processadas": count,
                "timestamp": datetime.now().isoformat()
            },
            status=201
        )
