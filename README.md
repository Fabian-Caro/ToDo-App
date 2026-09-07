# Tasks API

API REST para administrar tareas, construida con FastAPI y organizada mediante CQRS y vertical slices.

## Estado actual

La API implementa:

- Listado de tareas con filtrado, ordenamiento y paginación offset.
- Búsqueda paginada por título.
- Consulta individual de una tarea.
- Creación, reemplazo completo (`PUT`), actualización parcial (`PATCH`) y eliminación.
- Enlaces HATEOAS para navegar colecciones y descubrir acciones disponibles.
- Respuestas HTTP coherentes: `201 Created`, `200 OK`, `204 No Content`, `404 Not Found` y `422 Unprocessable Entity`.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/api/v1/tasks` | Lista tareas con filtros, ordenamiento y paginación. |
| `GET` | `/api/v1/tasks/search` | Busca tareas por título con paginación. |
| `GET` | `/api/v1/tasks/{task_id}` | Obtiene una tarea. |
| `POST` | `/api/v1/tasks` | Crea una tarea. |
| `PUT` | `/api/v1/tasks/{task_id}` | Reemplaza el estado editable completo. |
| `PATCH` | `/api/v1/tasks/{task_id}` | Actualiza uno o varios campos editables. |
| `DELETE` | `/api/v1/tasks/{task_id}` | Elimina una tarea. |

## Arquitectura

```text
features/tasks/
├── queries/
│   ├── list_tasks/
│   ├── search_tasks/
│   └── get_task/
├── commands/
│   ├── create_task/
│   ├── update_task/
│   ├── patch_task/
│   └── delete_task/
└── shared/
    └── links.py

infrastructure/
└── fake_db.py
```

Cada slice contiene sus propios modelos de request y response, endpoint y handler.

## Próximo objetivo

Migrar la persistencia temporal basada en `FAKE_DB` a SQLite. La meta es conservar el comportamiento actual de la API mientras se introduce una capa de repositorio y consultas SQL reales.

## Flujo de ramas

Las ramas permanentes son:

- `main`: versión estable y lista para producción.
- `develop`: rama de integración del trabajo en curso.

Ramas temporales:

- `feat/<nombre>`: nuevas funcionalidades; nacen de `develop` y vuelven a `develop`.
- `release/<version>`: preparación de una versión; nace de `develop` y se integra en `main` y `develop`.
- `hotfix/<nombre>`: correcciones urgentes; nacen de `main` y se integran en `main` y `develop`.
- `docs/<nombre>`: cambios exclusivamente documentales; nacen de `develop`.

La migración inicial puede desarrollarse en:

```text
feat/sqlite-migration
```