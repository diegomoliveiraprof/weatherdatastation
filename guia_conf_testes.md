# Guia de configuração para testes Django + PostgreSQL 

## 1. Instalação do PostgreSQL

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl enable postgresql
sudo systemctl start postgresql
```



## 2. Configuração do Banco

Entrar no PostgreSQL:

```bash
sudo -u postgres psql
```

Criar banco e usuário:

```sql
CREATE DATABASE wds_db;
CREATE USER wds_user WITH PASSWORD '123!@#wdstg';
GRANT ALL PRIVILEGES ON DATABASE wds_db TO wds_user;
ALTER ROLE wds_user SET client_encoding TO 'utf8';
ALTER ROLE wds_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE wds_user SET timezone TO 'UTC';
\q
```

Configurações adicionais:

Entrar no PostgreSQL:

```bash
sudo -u postgres psql
```

```sql
\c wds_db
GRANT USAGE, CREATE ON SCHEMA public TO wds_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO wds_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO wds_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO wds_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO wds_user;
\q
```



## 3. Preparar servidor com Python e dependências

```bash
sudo apt update && sudo apt install python3-pip python3-venv libpq-dev nginx curl -y
```

## 

## 4. Clonar o projeto

```bash
mkdir /var/www/wds
cd /var/www/wds   
git clone https://github.com/diegomoliveiraprof/weatherdatastation.git   
mv weatherdatastation/* .   
```



## 5. Configurar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```



## 6. Ajustes no settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wds_db',
        'USER': 'wds_user',
        'PASSWORD': '123!@#wdstg',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['*','127.0.0.1','localhost']
```



## 7. Migrações e superusuário

```bash
python manage.py makemigrations
python manage.py makemigrations WDS
python manage.py migrate
python manage.py createsuperuser
```



## 8. Rodar servidor Django



```bash
python3 manage.py runserver 0.0.0.0:8000
```

**Aviso importante**   Nesta configuração, o serviço só estará disponível **enquanto o comando** `python3 manage.py runserver 0.0.0.0:8000` estiver em execução. Essa abordagem é adequada apenas para **testes e desenvolvimento**, pois o servidor interno do Django não foi projetado para lidar com carga de produção ou oferecer recursos avançados de segurança.

Para colocar a aplicação em um **ambiente de produção**, é necessário configurar serviços adicionais como **Gunicorn** (WSGI) e **Nginx** (proxy reverso), além de ajustes de permissões, logs e HTTPS.
