#!/bin/bash

# Script para automatizar el despliegue de modelos y scripts de machine learning en Alphapp

# Variables de configuración
ML_COMPONENTS_DIR="ml-components"
MODELS_DIR="$ML_COMPONENTS_DIR/models"
SCRIPTS_DIR="$ML_COMPONENTS_DIR/scripts"
DATA_DIR="$ML_COMPONENTS_DIR/data"
DEPLOYMENT_DIR="/var/www/alphapp/ml"  # Directorio de destino en el servidor
LOG_FILE="/var/log/alphapp/ml_deploy.log"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Función para imprimir mensajes con timestamp
log() {
  echo "$TIMESTAMP - $1" | tee -a "$LOG_FILE"
}

# Verificar si los directorios existen
if [ ! -d "$ML_COMPONENTS_DIR" ]; then
  log "Error: El directorio '$ML_COMPONENTS_DIR' no existe."
  exit 1
fi

if [ ! -d "$DEPLOYMENT_DIR" ]; then
  log "Error: El directorio de despliegue '$DEPLOYMENT_DIR' no existe."
  exit 1
fi

# Desplegar modelos
log "Iniciando despliegue de modelos..."
if [ -d "$MODELS_DIR" ]; then
  find "$MODELS_DIR" -type d -print0 | while IFS= read -r -d $'\0' dir; do
    model_name=$(basename "$dir")
    log "Desplegando modelo: $model_name"
    cp -r "$dir" "$DEPLOYMENT_DIR"  # Ejemplo: copiar los directorios del modelo
    if [ $? -ne 0 ]; then
       log "Error: Fallo al desplegar el modelo: $model_name"
    fi
  done
else
  log "Advertencia: No se encontró el directorio de modelos '$MODELS_DIR'."
fi

# Desplegar scripts de Python
log "Iniciando despliegue de scripts..."
if [ -d "$SCRIPTS_DIR" ]; then
    find "$SCRIPTS_DIR" -maxdepth 1 -type f -name "*.py" -print0 | while IFS= read -r -d $'\0' script; do
      script_name=$(basename "$script")
      log "Desplegando script: $script_name"
      cp "$script" "$DEPLOYMENT_DIR"  # Ejemplo: copiar los scripts
      if [ $? -ne 0 ]; then
        log "Error: Fallo al desplegar el script: $script_name"
      fi

      # Hacer los scripts ejecutables
      chmod +x "$DEPLOYMENT_DIR/$script_name"
   done
else
    log "Advertencia: No se encontró el directorio de scripts '$SCRIPTS_DIR'."
fi

# Desplegar datos para pruebas
log "Iniciando despliegue de datos para pruebas..."
if [ -d "$DATA_DIR/test_data/processed" ]; then
  find "$DATA_DIR/test_data/processed" -type f -name "*.csv" -print0 | while IFS= read -r -d $'\0' file; do
    file_name=$(basename "$file")
      log "Desplegando archivo de datos: $file_name"
      cp "$file" "$DEPLOYMENT_DIR"  # Ejemplo: copiar los archivos de datos
      if [ $? -ne 0 ]; then
        log "Error: Fallo al desplegar el archivo de datos: $file_name"
      fi
  done
else
    log "Advertencia: No se encontró el directorio de datos para pruebas '$DATA_DIR/test_data/processed'."
fi

log "Despliegue finalizado."
exit 0


