# TODO

## Repositorio y flujo de trabajo

- [x] Crear el repositorio remoto.
- [ ] Añadir `README.md` y `TODO.md`.
- [ ] Crear la rama `develop` desde `main`.
- [ ] Configurar `main` y `develop` como ramas base.
- [ ] Crear la rama `feature/sqlite-migration` desde `develop`.
- [ ] Definir una convención de commits.

## Migración de `FAKE_DB` a SQLite

- [ ] Identificar las operaciones actuales contra `FAKE_DB`.
- [ ] Elegir la librería de persistencia: SQLAlchemy o SQLModel.
- [ ] Configurar una base de datos SQLite local.
- [ ] Crear el modelo persistente de `Task`.
- [ ] Crear el esquema inicial de la base de datos.
- [ ] Diseñar un repositorio de tareas.
- [ ] Migrar `create_task`.
- [ ] Migrar `get_task`.
- [ ] Migrar `list_tasks` con filtro, ordenamiento y paginación SQL.
- [ ] Migrar `search_tasks`.
- [ ] Migrar `update_task`, `patch_task` y `delete_task`.
- [ ] Eliminar `FAKE_DB` cuando todos los casos de uso dependan del repositorio.
- [ ] Verificar manualmente que los enlaces HATEOAS conservan las rutas correctas.

## Calidad posterior

- [ ] Añadir pruebas de integración mínimas para los flujos principales.
- [ ] Documentar ejemplos de request y response en OpenAPI.
- [ ] Evaluar autenticación y autorización.
- [ ] Evaluar control de concurrencia con versión o `ETag`.
- [ ] Evaluar migración de SQLite a PostgreSQL.