# PROJECT TITAN

Plataforma modular de inteligencia deportiva y análisis de mercados de apuestas.
Modo inicial: análisis y registro manual; no ejecuta apuestas.

## Stack inicial
- Python 3.12+
- FastAPI
- PostgreSQL (Neon recomendado para comenzar)
- SQLAlchemy 2 + Alembic (preparado para incorporar migraciones)
- Pydantic Settings
- httpx
- pytest

## Estructura
- `app/api`: endpoints HTTP
- `app/core`: configuración y utilidades comunes
- `app/connectors`: contratos y adaptadores de proveedores
- `app/domain`: entidades y esquemas normalizados
- `app/services`: lógica de negocio
- `app/jobs`: tareas programadas/importaciones
- `tests`: pruebas

## Inicio local
1. Copiar `.env.example` a `.env` y completar valores.
2. Crear entorno virtual e instalar dependencias:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Ejecutar:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Abrir `/docs` para la documentación interactiva.

## Despliegue económico propuesto
- API: Railway Hobby (vigilar consumo y establecer alertas/límites).
- PostgreSQL: Neon Free para prototipo; pasar a plan de pago con backups/SLA antes de depender de producción.
- Frontend: Cloudflare Pages o similar cuando se incorpore React.
- Código: repositorio privado GitHub.

Los planes gratuitos son para prototipos y pueden tener límites, suspensión o ausencia de garantías de disponibilidad. No guardar datos críticos sin backups.

## Variables
Ver `.env.example`. Nunca subir `.env`, claves API ni credenciales al repositorio.

## Principios de datos
- Guardar `provider`, `provider_event_id`, `captured_at` y `raw_payload`.
- No mezclar cuotas de casas tradicionales con precios de exchange.
- No sobrescribir snapshots históricos.
- Marcar datos faltantes; nunca inventar cuotas, lesiones ni estadísticas.
- Cada predicción futura debe guardar timestamp y versión del modelo.
