#!/bin/bash
set -e

AUTH_USER=${AUTH_USER:-'admin'}
AUTH_PASS=${AUTH_PASS:-'pass'}

htpasswd -b -c /etc/nginx/.htpasswd $AUTH_USER $AUTH_PASS

cp /var/config/nginx/nginx.conf /etc/nginx/nginx.conf
rm -rf /etc/nginx/sites-enabled/*
ln -s /var/config/nginx/app.conf /etc/nginx/sites-enabled/

/usr/bin/supervisord -n

exec "$@"
