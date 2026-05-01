# 🌦️ Weather Data System (WDS)

Este projeto é uma aplicação **Django + Django REST Framework** para coleta, armazenamento e exposição de dados meteorológicos provenientes de sensores como DHT22, BME280, MQ-series, GY30, UV GYML8511, entre outros.

---

## 🚀 Funcionalidades

- Upload de arquivos **CSV** com leituras de sensores.
- Conversão automática de valores inválidos (`nan`) para `NULL`.
- API REST para consulta dos dados meteorológicos.
- Filtros avançados via **django-filter** (por temperatura, direção do vento, etc.).
- Documentação interativa da API via **Swagger UI** e **ReDoc**.
- Integração com PostgreSQL para persistência dos dados.

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

- O upload de CSV exige autenticação via **Token**.
- Exemplo de requisição:
  ```bash
  curl -X POST https://end_IP:8000/api/upload/ \
    -H "Authorization: Token SEU_TOKEN_AQUI" \
    -F "file=@dados_teste.csv"
