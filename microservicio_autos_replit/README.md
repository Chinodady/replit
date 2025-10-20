# Microservicio: Catálogo de Autos (Flask)

## Estructura
- `app.py`: servicio Flask con endpoints REST y filtros por query.
- `requirements.txt`: dependencias.

## Ejecutar en Replit
1. Crea un nuevo Repl (Python o Flask).
2. Sube `app.py` y `requirements.txt`.
3. Pulsa **Run**. Copia la URL pública.

## Endpoints
- `GET /` -> healthcheck.
- `GET /api/autos` -> lista autos. Filtros: `marca`, `modelo`, `color`, `anio_min`, `anio_max`, `precio_max`.
- `GET /api/autos/<id>` -> detalle por ID.

## Ejemplos
- Todos: `/api/autos`
- Filtrado: `/api/autos?marca=Toyota&anio_min=2019&precio_max=300000`
