## HTTPS com IP público Certificado autoassinado

1. **Certificado autoassinado (self-signed)**

   - Gera um certificado SSL no próprio servidor.
   - Funciona para criptografar o tráfego, mas os navegadores vão mostrar aviso de "Conexão não segura" porque não é emitido por uma autoridade confiável.

   Exemplo de geração:

   ```bash
   sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout /etc/ssl/private/wds.key \
     -out /etc/ssl/certs/wds.crt
   ```

   

   **Configuração no Nginx:**

   Edite seu arquivo `/etc/nginx/sites-available/wds` e adicione um bloco para **443**:

   ```nginx
   server {
       listen 80;
       server_name SEU_IP;
   
       # Redirecionar todo HTTP para HTTPS
       return 301 https://$host$request_uri;
   }
   
   server {
       listen 443 ssl;
       server_name SEU_IP;
   
       ssl_certificate /etc/ssl/certs/wds.crt;
       ssl_certificate_key /etc/ssl/private/wds.key;
   
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

   

   **Aplicar configuração**

   ```bash
   sudo nginx -t
   sudo systemctl restart 
   ```



## Renovação manual do certificado autoassinado

1. **Remover ou arquivar os certificados antigos**   (opcional, mas ajuda na organização)

   ```bash
   sudo mv /etc/ssl/private/wds.key /etc/ssl/private/wds.key.old
   sudo mv /etc/ssl/certs/wds.crt /etc/ssl/certs/wds.crt.old
   ```

2. **Gerar novos certificados**   Ajuste o número de dias conforme desejar (exemplo: 3 anos = 1095 dias):

   ```bash
   sudo openssl req -x509 -nodes -days 1095 -newkey rsa:2048 \
     -keyout /etc/ssl/private/wds.key \
     -out /etc/ssl/certs/wds.crt
   ```

   > No campo *Common Name (CN)*, você pode colocar o IP público ou interno).

3. **Verificar permissões**

   - A chave privada deve ser acessível apenas pelo root:

     ```bash
     sudo chmod 600 /etc/ssl/private/wds.key
     ```

   - O certificado pode ser lido por todos:

     ```bash
     sudo chmod 644 /etc/ssl/certs/wds.crt
     ```

4. **Recarregar Nginx**

   ```bash
   sudo nginx -t
   sudo systemctl reload nginx
   ```

## 
