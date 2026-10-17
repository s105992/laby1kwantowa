#!/usr/bin/env sh
set -eu
[ -f .env ] || cp .env.example .env
docker compose up -d --build
printf '\nJupyterLab: http://127.0.0.1:8888\n'
printf 'Token znajduje sie w pliku .env (JUPYTER_TOKEN).\n'
