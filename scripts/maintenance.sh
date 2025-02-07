#!/bin/bash

# Script de mantenimiento para Alphapp

set -e  # Terminar el script si algún comando falla

# Función para imprimir mensajes
function print_message() {
    echo "========================================"
    echo "$1"
    echo "========================================"
}

print_message "Iniciando tareas de mantenimiento..."

# Limpiar archivos temporales
print_message "Limpiando archivos temporales..."
find . -name "*.pyc" -delete

# Actualizar dependencias del backend
print_message "Actualizando dependencias del backend..."
pip install --upgrade -r requirements.txt

# Navegar al directorio del frontend y actualizar dependencias
cd src/frontend
print_message "Actualizando dependencias del frontend..."
npm update

# Realizar respaldo de la base de datos (ejemplo)
# print_message "Realizando respaldo de la base de datos..."
# pg_dump -U user -h host -p port database > backup.sql

print_message "Tareas de mantenimiento completadas."

