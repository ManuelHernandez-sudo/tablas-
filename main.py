import psycopg2

# Conexión a la base de datos PostgreSQL
# Asegúrate de tener PostgreSQL corriendo en Docker o localmente
# Cambia los valores de conexión según tu configuración
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="yourpassword",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# 1. Crear tablas
cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        precio NUMERIC(10,2) NOT NULL
    );
""")

print("Tablas 'clientes' y 'productos' creadas ✅")

# 2. Agregar columnas nuevas
cur.execute("ALTER TABLE clientes ADD COLUMN IF NOT EXISTS email VARCHAR(100);")
cur.execute("ALTER TABLE productos ADD COLUMN IF NOT EXISTS stock INT DEFAULT 0;")
print("Columnas nuevas agregadas ✅")

# 3. Renombrar columnas
cur.execute("ALTER TABLE clientes RENAME COLUMN nombre TO nombre_completo;")
cur.execute("ALTER TABLE productos RENAME COLUMN nombre TO descripcion;")
print("Columnas renombradas ✅")

# 4. Eliminar columnas
cur.execute("ALTER TABLE clientes DROP COLUMN IF EXISTS email;")
print("Columna eliminada de clientes ✅")

# 5. Agregar un CHECK
cur.execute("ALTER TABLE productos ADD CONSTRAINT precio_positivo CHECK (precio > 0);")
print("CHECK agregado a productos ✅")

# 6. Eliminar una tabla
cur.execute("DROP TABLE IF EXISTS clientes;")
print("Tabla 'clientes' eliminada ✅")

# Guardar cambios
conn.commit()

# Cerrar conexión
cur.close()
conn.close()
print("Conexión cerrada 🚪")
