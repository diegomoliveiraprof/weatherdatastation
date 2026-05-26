# 🌦️ API - Weather Data Station (WDS)

Este projeto é uma aplicação **Django + Django REST Framework** para coleta, armazenamento e exposição de dados meteorológicos provenientes de sensores como DHT22, BME280, MQ-series, GY30, UV GYML8511, entre outros.

---

## 🚀 Funcionalidades   
Upload de arquivos JSON com leituras de sensores.

API REST para consulta dos dados meteorológicos.

Filtros avançados via django-filter (por temperatura, direção do vento, etc.).

Documentação interativa da API via Swagger UI e ReDoc.

Integração com PostgreSQL para persistência dos dados.

---

## 📂 Estrutura principal

- `WDS/models.py` → Modelo `WeatherData` com todos os campos dos sensores.
- `WDS/views.py` → Endpoints de upload e listagem dos dados.
- `WDS/serializers.py` → Serialização dos dados para JSON.
- `WDS/urls.py` → Rotas da API e documentação.
- `requirements.txt` → Dependências do projeto.

---

## 📄 Endpoints

- `POST /api/upload/` → Upload de arquivo CSV (autenticado).
- `GET /api/weather/` → Consulta dos dados meteorológicos (sem autenticação).
- `GET /api/schema/` → Schema OpenAPI em JSON.
- `GET /api/docs/` → Swagger UI.
- `GET /api/redoc/` → ReDoc.

---

## 🔑 Autenticação
O upload de arquivos JSON exige autenticação via Token.

Exemplo de requisição
```Código
curl -X POST http://seu_ip:8000/api/upload/ \
  -H "Authorization: Token seu_token" \
  -H "Content-Type: application/json" \
  -d '{
  "DataHora": "2026-05-21 13:08:25",
  "DHT22_Temp": "27.5",
  "DHT22_Umid": "53.8",
  "DHT22_IndCalor": "29.1",
  "MQ2": "0.02",
  "BME280_Temp": "26.9",
  "BME280_Umi": "55.1",
  "BME280_Press": "1013.25",
  "BME280_Alti": "850.0",
  "GY30_Lux": "320.5",
  "GY30_ClassLux": "Moderado",
  "UVGYML8511_UV": "5.2",
  "UVGYML8511_Tensao": "1.8",
  "UVGYML8511_Saida": "0.75",
  "MQ137_PPMMedia": "0.15",
  "MQ137_PPMInstant": "0.20",
  "UVcjmcu_IndiUV": "3.1",
  "MQ3": "0.05",
  "MQ4": "0.08",
  "MQ7": "0.12",
  "Pluvio_MM": "2.5",
  "Anemo_VelMS": "3.2",
  "Anemo_VelKMH": "11.5",
  "Anemo_Grau": "180.0",
  "Anemo_Direcao": "Sul"
}'
  ```
---

## 📚 Guias de Configuração
Este projeto pode ser executado em diferentes ambientes, dependendo da finalidade:

[Guia para ambiente de testes](https://github.com/diegomoliveiraprof/weatherdatastation/blob/main/guia_conf_testes.md)  
Explica como configurar rapidamente o projeto para rodar com python3 manage.py runserver 0.0.0.0:8000, ideal para desenvolvimento e validação inicial.

[Guia para ambiente de produção / deploy](https://github.com/diegomoliveiraprof/weatherdatastation/blob/main/guia_deploy.md)  
Detalha como configurar PostgreSQL, Gunicorn e Nginx para rodar o sistema de forma estável e segura em servidores Linux.

[HTTPS Certificado autoassinado](https://github.com/diegomoliveiraprof/weatherdatastation/blob/main/https.md)    
Configuração do certificado para HTTPS autoassinado.
