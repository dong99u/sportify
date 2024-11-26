#!/bin/bash

# 도메인과 이메일 설정
domains=(hufsthon.site www.hufsthon.site)
email="qkrehdrb0813@gmail.com" # SSL 인증서 만료 알림을 받을 이메일

# certbot 디렉토리 생성
mkdir -p ./certbot/conf
mkdir -p ./certbot/www

# SSL 인증서 발급
if [ ! -e "./certbot/conf/live/$domains" ]; then
  echo "### Creating dummy certificate for $domains ..."
  docker-compose run --rm --entrypoint "\
    openssl req -x509 -nodes -newkey rsa:4096 -days 1\
      -keyout '/etc/letsencrypt/live/$domains/privkey.pem' \
      -out '/etc/letsencrypt/live/$domains/fullchain.pem' \
      -subj '/CN=localhost'" certbot

  echo "### Starting nginx ..."
  docker-compose up --force-recreate -d nginx

  echo "### Deleting dummy certificate for $domains ..."
  docker-compose run --rm --entrypoint "\
    rm -Rf /etc/letsencrypt/live/$domains && \
    rm -Rf /etc/letsencrypt/archive/$domains && \
    rm -Rf /etc/letsencrypt/renewal/$domains.conf" certbot

  echo "### Requesting Let's Encrypt certificate for $domains ..."
  docker-compose run --rm --entrypoint "\
    certbot certonly --webroot -w /var/www/certbot \
      --email $email \
      --agree-tos \
      --no-eff-email \
      -d ${domains[0]} -d ${domains[1]}" certbot

  echo "### Reloading nginx ..."
  docker-compose exec nginx nginx -s reload
fi