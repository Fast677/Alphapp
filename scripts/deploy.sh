#!/bin/bash

# Script de despliegue para Alphapp

# Configuración de variables
REPO_URL="https://github.com/Fast677/Alphapp.git"
BRANCH="main"
DEPLOY_DIR="/var/www/alphapp"

# Clonar el repositorio y cambiar al directorio de despliegue
git clone -b $BRANCH $REPO_URL $DEPLOY_DIR

# Navegar al directorio de despliegue
cd $DEPLOY_DIR

# Instalar dependencias
echo "Instalando dependencias..."
npm install

# Construir la aplicación
echo "Construyendo la aplicación..."
npm run build

# Reiniciar el servidor (Por ejemplo, usando pm2)
echo "Reiniciando el servidor..."
pm2 restart alphapp

echo "Despliegue completado con éxito!"


