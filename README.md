# 🌦️ Weather Data System (WDS)

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
POST /api/upload/ HTTP/1.1
Host: SEU_IP:8000
Authorization: Token SEU_TOKEN
Content-Type: application/json

{
  "DHT22_Temp": "27.50",
  "DHT22_Umid": "53.80",
  "DataHora": "2026-05-21 13:08:25",
  ...
}

  ```
## 📚 Guias de Configuração
Este projeto pode ser executado em diferentes ambientes, dependendo da finalidade:

Guia para ambiente de testes  
Explica como configurar rapidamente o projeto para rodar com python3 manage.py runserver 0.0.0.0:8000, ideal para desenvolvimento e validação inicial.

Guia para ambiente de produção / deploy  
Detalha como configurar PostgreSQL, Gunicorn e Nginx para rodar o sistema de forma estável e segura em servidores Linux.

## 📚 Guias de Configuração
Este projeto pode ser executado em diferentes ambientes, dependendo da finalidade:

[Guia para ambiente de testes](https://github.com/diegomoliveiraprof/weatherdatastation/blob/main/guia_conf_testes.md)  
Explica como configurar rapidamente o projeto para rodar com python3 manage.py runserver 0.0.0.0:8000, ideal para desenvolvimento e validação inicial.

[Guia para ambiente de produção / deploy](https://github.com/diegomoliveiraprof/weatherdatastation/blob/main/guia_deploy.md)  
Detalha como configurar PostgreSQL, Gunicorn e Nginx para rodar o sistema de forma estável e segura em servidores Linux.
