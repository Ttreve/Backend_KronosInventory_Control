# Kronos Inventory Control - Backend

API en FastAPI + SQLAlchemy + Alembic sobre MySQL.

## Requisitos
Python 3.12 o superior y MySQL con una base `kronos_inventory`.

## Instalación
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env      # luego editar DATABASE_URL con su usuario y contraseña
```
En la contraseña, `#` se escribe `%23` y `@` se escribe `%40`.

## Base de datos
```sql
CREATE DATABASE IF NOT EXISTS kronos_inventory CHARACTER SET utf8mb4;
```
```powershell
alembic upgrade head
```

## Ejecutar
```powershell
uvicorn app.main:app --reload
```
Documentación en `/docs`; estado en `/health` y `/health/ready`.

## Pruebas
```powershell
pytest
```
Requiere el archivo `.env` creado.
