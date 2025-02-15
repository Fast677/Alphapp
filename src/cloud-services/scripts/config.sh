#!/bin/bash
# Script para automatizar la configuración de los servicios en la nube de Alphapp

# Variables de entorno
export APP_HOME="/opt/alphapp/cloud-services"
export APP_USER="alphapp"
export ENVIRONMENT="production" # o "development", "testing"
export DATABASE_URL="postgres://user:password@host:port/database"
export API_KEY="your_api_key"

# Funciones de utilidad
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

error() {
  log "ERROR: $1"
  exit 1
}

# 1. Cargar variables de entorno desde un archivo (opcional)
log "Cargando variables de entorno..."
if [ -f ".env" ]; then
  log "Cargando variables desde .env"
  set -a
  source .env
  set +a
fi

# 2. Configurar la base de datos
log "Configurando la base de datos..."
# (Aquí se realizarían tareas de configuración de la base de datos)
# Ejemplo: Crear la base de datos si no existe
# sudo -u postgres psql -c "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME;"

# 3. Generar certificados SSL (opcional)
log "Generando certificados SSL..."
# (Aquí se generarían certificados SSL si es necesario)
# Ejemplo: Usando OpenSSL
# sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $APP_HOME/ssl/private.key -out $APP_HOME/ssl/certificate.crt

# 4. Establecer permisos
log "Estableciendo permisos..."
sudo chown -R "$APP_USER":"$APP_USER" "$APP_HOME"

# 5. Configuración específica del entorno
log "Configuración específica del entorno ($ENVIRONMENT)..."
# (Aquí se realizarían configuraciones específicas para el entorno, como establecer variables de entorno diferentes)
if [ "$ENVIRONMENT" == "production" ]; then
  log "Configurando para producción..."
  # Ejemplo: Establecer una variable de entorno específica para producción
  export DEBUG=False
elif [ "$ENVIRONMENT" == "development" ]; then
  log "Configurando para desarrollo..."
  # Ejemplo: Establecer una variable de entorno específica para desarrollo
  export DEBUG=True
fi

# 6. Reiniciar los servicios (si es necesario)
log "Reiniciando los servicios..."
# (Aquí se reiniciarían los servicios para aplicar la nueva configuración)
# Ejemplo con systemctl:
# sudo systemctl restart alphapp-cloud-service.service

log "Configuración completada exitosamente."
exit 0
