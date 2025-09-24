# Proyecto PostgreSQL con Python

Este proyecto muestra cómo conectarse a una base de datos PostgreSQL desde Python y aplicar operaciones **DDL**.

---

## 🚀 Requisitos
- Tener instalado **Docker** o PostgreSQL en local.
- Contenedor PostgreSQL corriendo (ejemplo con Docker):

```bash
docker run --name postgres-db -e POSTGRES_PASSWORD=yourpassword -p 5432:5432 -d postgres
```

- Instalar librería para Python:
```bash
pip install psycopg2
```

---

## 📌 Operaciones realizadas

1. **Creación de tablas**
   - `clientes` con `id` y `nombre`.
   - `productos` con `id`, `nombre` y `precio`.

2. **Agregar columnas nuevas**
   - `clientes.email`
   - `productos.stock`

3. **Renombrar columnas**
   - `clientes.nombre → nombre_completo`
   - `productos.nombre → descripcion`

4. **Eliminar columnas**
   - Eliminada `clientes.email`

5. **Agregar un CHECK**
   - `productos.precio > 0`

6. **Eliminar una tabla**
   - Eliminada tabla `clientes`

---

## ▶️ Ejecución
Ejecutar el script:

```bash
python main.py
```

Verás en consola los mensajes de confirmación de cada operación.

---
