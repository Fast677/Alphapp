#!/bin/bash

# Script de despliegue para Alphapp

set -e  # Terminar el script si algún comando falla

# Configuración de variables
REPO_URL="https://github.com/Fast677/Alphapp.git"
BRANCH="main"
DEPLOY_DIR="/var/www/alphapp"

# Función para imprimir mensajes
function print_message() {
    echo "========================================"
    echo "$1"
    echo "========================================"
}

print_message "Clonando el repositorio..."
git clone -b $BRANCH $REPO_URL $DEPLOY_DIR

cd $DEPLOY_DIR

print_message "Instalando dependencias..."
npm install

print_message "Construyendo la aplicación..."
npm run build

print_message "Reiniciando el servidor..."
pm2 restart alphapp

print_message "Despliegue completado con éxito!"


