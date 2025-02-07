#!/bin/bash

# Script para configurar el entorno de desarrollo para Alphapp

set -e  # Terminar el script si algún comando falla

# Función para imprimir mensajes
function print_message() {
    echo "========================================"
    echo "$1"
    echo "========================================"
}

print_message "Configurando el entorno de desarrollo..."

# Clonar el repositorio si no existe
REPO_URL="https://github.com/Fast677/Alphapp.git"
if [ ! -d "Alphapp" ]; then
    print_message "Clonando el repositorio..."
    git clone $REPO_URL
fi

cd Alphapp

# Crear y activar entorno virtual para el backend
print_message "Creando y activando entorno virtual para el backend..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias del backend
print_message "Instalando dependencias del backend..."
pip install --upgrade pip
pip install -r requirements.txt

# Navegar al directorio del frontend
cd src/frontend

# Instalar dependencias del frontend
print_message "Instalando dependencias del frontend..."
npm install

print_message "Configuración del entorno de desarrollo completada."
