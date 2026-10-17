if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
}
docker compose up -d --build
Write-Host ""
Write-Host "JupyterLab: http://127.0.0.1:8888"
Write-Host "Token znajduje sie w pliku .env (JUPYTER_TOKEN)."
