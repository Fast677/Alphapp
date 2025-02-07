#!/bin/bash

# Script para ejecutar pruebas en Alphapp

set -e  # Terminar el script si algún comando falla

# Función para imprimir mensajes
function print_message() {
    echo "========================================"
    echo "$1"
    echo "========================================"
}

print_message "Iniciando pruebas..."

# Ejecutar pruebas del backend
print_message "Ejecutando pruebas del backend..."
cd src/backend
python -m unittest discover tests

# Ejecutar pruebas del frontend (si aplica)
print_message "Ejecutando pruebas del frontend..."
cd ../../src/frontend
npm test

print_message "Pruebas completadas."
