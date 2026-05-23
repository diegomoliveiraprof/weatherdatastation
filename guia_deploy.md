# Guia de Deploy Django + PostgreSQL + Gunicorn + Nginx

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
CREATE USER wds_user WITH PASSWORD 'sua_senha';
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
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['*','127.0.0.1','localhost']
DEBUG = False
```



## 7. Migrações e superusuário

```bash
python manage.py makemigrations
python manage.py makemigrations WDS
python manage.py migrate
python manage.py createsuperuser
```



## 8. Coletar arquivos estáticos

```bash
python manage.py collectstatic
```



## 9. Permissões

```bash
sudo chown -R www-data:www-data /var/www/wds
sudo chmod -R 755 /var/www/wds
sudo chown -R www-data:www-data /var/www/wds/staticfiles
mkdir /var/www/wds/media
sudo chown -R www-data:www-data /var/www/wds/media
sudo chmod -R 755 /var/www/wds/media
```



## 10. Instalar e configurar Gunicorn

```bash
pip install gunicorn
```

Arquivo `/etc/systemd/system/wds.service`:

```ini
[Unit]
Description=Gunicorn instance for WDS
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/wds
Environment="PATH=/var/www/wds/venv/bin"
ExecStart=/var/www/wds/venv/bin/gunicorn --workers 3 --bind unix:/var/www/wds/wds.sock wds_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Ativar serviço:

```bash
sudo systemctl daemon-reload
sudo systemctl enable wds
sudo systemctl start wds
```



## 11. Configurar Nginx como proxy reverso

Arquivo `/etc/nginx/sites-available/wds`:



```nginx
server {
    listen 80;
    server_name 192.168.68.57;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /var/www/wds/staticfiles/;
    }

    location /media/ {
        alias /var/www/wds/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/wds/wds.sock;
    }
}
```



Ativar site:

```bash
sudo ln -s /etc/nginx/sites-available/wds /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart 
```

