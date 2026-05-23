from datetime import datetime
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import WeatherData
from .serializers import WeatherDataSerializer


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
    data = django_filters.DateFilter(field_name="hora", lookup_expr="date", label="Data")
    data_range = django_filters.DateFromToRangeFilter(field_name="hora", label="Data Intervalo")
    hora_only = django_filters.TimeFilter(field_name="hora", lookup_expr="time", label="Horário")
    temperatura_range = django_filters.RangeFilter(field_name="dht22_temp", label="Temp DHT22 Intervalo")
    umidade_range = django_filters.RangeFilter(field_name="dht22_umid", label="Umidade DHT22 Intervalo")
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
        data = request.data  # JSON enviado pelo Arduino

        try:
            hora_dt = datetime.strptime(data.get("DataHora"), "%Y-%m-%d %H:%M:%S")
        except Exception:
            return Response({"error": "Formato de DataHora inválido"}, status=400)

        WeatherData.objects.create(
            hora=hora_dt,
            dht22_temp=safe_float(data.get("DHT22_Temp")),
            dht22_umid=safe_float(data.get("DHT22_Umid")),
            dht22_ind_calor=safe_float(data.get("DHT22_IndCalor")),
            mq2=safe_float(data.get("MQ2")),
            bme280_temp=safe_float(data.get("BME280_Temp")),
            bme280_umi=safe_float(data.get("BME280_Umi")),
            bme280_press=safe_float(data.get("BME280_Press")),
            bme280_alti=safe_float(data.get("BME280_Alti")),
            gy30_lux=safe_float(data.get("GY30_Lux")),
            gy30_class_lux=data.get("GY30_ClassLux"),
            uv_gyml8511_uv=safe_float(data.get("UVGYML8511_UV")),
            uv_gyml8511_tensao=safe_float(data.get("UVGYML8511_Tensao")),
            uv_gyml8511_saida=safe_float(data.get("UVGYML8511_Saida")),
            mq137_ppm_media=safe_float(data.get("MQ137_PPMMedia")),
            mq137_ppm_instant=safe_float(data.get("MQ137_PPMInstant")),
            uvcjmcu_indiuv=safe_float(data.get("UVcjmcu_IndiUV")),
            mq3=safe_float(data.get("MQ3")),
            mq4=safe_float(data.get("MQ4")),
            mq7=safe_float(data.get("MQ7")),
            pluvio_mm=safe_float(data.get("Pluvio_MM")),
            anemo_vel_ms=safe_float(data.get("Anemo_VelMS")),
            anemo_vel_kmh=safe_float(data.get("Anemo_VelKMH")),
            anemo_grau=safe_float(data.get("Anemo_Grau")),
            anemo_direcao=data.get("Anemo_Direcao"),
        )

        return Response(
            {
                "status": "Upload realizado com sucesso",
                "linhas_processadas": 1,
                "timestamp": datetime.now().isoformat()
            },
            status=201
        )
