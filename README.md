# Proyecto IS2-2025-Grupo7

## 🏗️ Estado general del proyecto
- **Rama principal:** `main` (estable, contiene todo el código funcionando y testeado).  
- **Ramas de desarrollo:** `master`, `mi-cambio-producto`, `feature` (donde los compañeros suben sus cambios).  
- **Objetivo:** Integrar modelos, schemas, tests y migraciones de base de datos sin romper el código.

---

## ✅ Semana 1 – Modelo base, Git y estructura del proyecto
- Tareas completadas: 6/6 ✔️  
- Se creó la **estructura inicial del proyecto**:
  - Carpeta `backend/app/db/models` con modelo base `ProductoORM`.
  - Configuración inicial de Git.
  - Carpeta para tests.
  - Rama principal `main` creada y lista para integrar cambios.
- Documentación de la rama `main` como estable.

---

## ✅ Semana 2 – ORM + Domain + Schemas (modelo de datos completo)
- Tareas completadas: 0/4 ❌ (abiertas)  
- Cambios incorporados por los compañeros:
  - **Validación de unicidad** en `ProductoORM` (campos `nombre` y `sku`).
  - Creación de **Base declarativa** en `backend/app/db/base.py`.
  - Migraciones de Alembic configuradas (`alembic.ini` y `env.py`).
  - Esquemas Pydantic en `backend/app/schemas/producto.py`.
  - Tests agregados: `test_producto.py` en `backend/app/tests` y `backend/tests`.
  - Mappers entre modelos de dominio y ORM (`product_mapper.py`).
- Todo mergeado a `main` y testeado.

---

## 📂 Archivos importantes
- `backend/app/db/models/producto.py` – Modelo ProductoORM.
- `backend/app/db/base.py` – Base declarativa.
- `backend/app/schemas/producto.py` – Schemas Pydantic.
- `backend/app/mappers/product_mapper.py` – Mappers de dominio a ORM.
- `backend/app/tests/test_producto.py` y `backend/tests/test_producto.py` – Tests.
- `alembic.ini` y `backend/alembic/migrations/env.py` – Configuración de migraciones.
