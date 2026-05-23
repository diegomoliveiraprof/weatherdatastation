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

- O upload de JSON exige autenticação via **Token**.

- Exemplo de requisição:

  ```bash
   POST /api/upload/ HTTP/1.1
    Host: end_ip:8000
    Authorization: Token seu_token
    Content-Type: application/json
  
    {
      "DHT22_Temp":"27.50",
      "DHT22_Umid":"53.80",
      "DataHora":"2026-05-21 13:08:25",
      ...
    }

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
sudo systemctl start  postgresql
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
**Conceder permissão de criação no schema public**
```sql
--Ainda no console sql
\c wds_db

-- Permitir uso e criação no schema public
GRANT USAGE ON SCHEMA public TO wds_user;
GRANT CREATE ON SCHEMA public TO wds_user;

-- Permitir acesso a tabelas e sequências existentes
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO wds_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO wds_user;

-- Garantir que objetos futuros também fiquem acessíveis
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO wds_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO wds_user;
```

### 5. Sair do psql

```
\q
```

## 📄 Configuração no Django (`settings.py`)

Preparação do ambiente:
```bash
sudo apt update
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


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
   python manage.py makemigrations
   python manage.py makemigrations WDS
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
