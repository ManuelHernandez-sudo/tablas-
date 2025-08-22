create DATABASE importacion_vehiculos;
-- Crear base de datos
CREATE DATABASE importacion_vehiculos;

\c importacion_vehiculos;

-- ================================
-- TABLA: Lote de Importación
-- ================================
CREATE TABLE lote_importacion (
    codigo_lote VARCHAR(10) PRIMARY KEY,
    fecha_llegada DATE NOT NULL,
    pais_origen VARCHAR(50) NOT NULL
);

-- ================================
-- TABLA: Concesionario
-- ================================
CREATE TABLE concesionario (
    codigo_concesionario VARCHAR(10) PRIMARY KEY,
    nombre_comercial VARCHAR(100) NOT NULL,
    direccion VARCHAR(150),
    persona_contacto VARCHAR(100)
);

-- ================================
-- TABLA: Vehículo
-- ================================
CREATE TABLE vehiculo (
    numero_serie VARCHAR(20) PRIMARY KEY,
    modelo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    anio_fabricacion INT CHECK (anio_fabricacion >= 1900 AND anio_fabricacion <= EXTRACT(YEAR FROM CURRENT_DATE)),
    velocidad_maxima NUMERIC(5,2) CHECK (velocidad_maxima > 0),
    precio_declarado NUMERIC(12,2) CHECK (precio_declarado >= 0),
    codigo_lote VARCHAR(10) REFERENCES lote_importacion(codigo_lote) ON DELETE CASCADE,
    codigo_concesionario VARCHAR(10) REFERENCES concesionario(codigo_concesionario) ON DELETE SET NULL
);
