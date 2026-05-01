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
  ```



# Banco de dados

O projeto utiliza PostgreSQL

## 🛠️ Instalação do PostgreSQL

### Linux (Ubuntu/Debian)

```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Inicializar o banco:

```
sudo postgresql-setup initdb
sudo systemctl enable postgresql
sudo systemctl start 
```



## 🛠️ Configuração do Banco

### 1. Entrar no PostgreSQL

No terminal:

```
sudo -u postgres psql
```

### 2. Criar o banco de dados

```
CREATE DATABASE wds_db;
```

### 3. Criar o usuário

```
CREATE USER wds_user WITH PASSWORD 'sua_senha_segura';
```

### 4. Dar permissões ao usuário

```
ALTER ROLE wds_user SET client_encoding TO 'utf8';
ALTER ROLE wds_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE wds_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE wds_db TO wds_user;
```

### 5. Sair do psql

```
\q
```

## 📄 Configuração no Django (`settings.py`)

Adapte a seção `DATABASES`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wds_db',
        'USER': 'wds_user',
        'PASSWORD': 'sua_senha_segura',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```



## 🚀 Testar conexão

1. Rode as migrações:

   ```
   python manage.py migrate
   ```

2. Crie um superusuário:

   ```
   python manage.py createsuperuser
   ```

3. Inicie o servidor:

   ```
   python manage.py runserver
   ```

Se tudo estiver certo, o Django vai conectar ao PostgreSQL usando o usuário criado.
