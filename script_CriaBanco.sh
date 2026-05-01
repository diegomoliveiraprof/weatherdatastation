#!/bin/bash

# Atualiza pacotes
sudo apt update

# Instala PostgreSQL e contrib
sudo apt install -y postgresql postgresql-contrib

# Inicia serviço
sudo systemctl enable postgresql
sudo systemctl start postgresql

# Configura banco e usuário
sudo -u postgres psql <<EOF
CREATE DATABASE wds_db;
CREATE USER wds_user WITH PASSWORD 'sua_senha_segura';
ALTER ROLE wds_user SET client_encoding TO 'utf8';
ALTER ROLE wds_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE wds_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE wds_db TO wds_user;
EOF

echo "PostgreSQL instalado e configurado com banco 'wds_db' e usuário 'wds_user'"
