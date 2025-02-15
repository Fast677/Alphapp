#!/bin/bash
# Script para automatizar el despliegue de los servicios en la nube de Alphapp

# Variables de entorno (se pueden cargar desde un archivo .env)
export APP_HOME="/opt/alphapp/cloud-services"
export APP_USER="alphapp"
export ENVIRONMENT="production" # o "development", "testing"

# Funciones de utilidad
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

error() {
  log "ERROR: $1"
  exit 1
}

# 1. Preparación del entorno
log "Preparando el entorno de despliegue..."

# Asegurarse de que el usuario de la aplicación existe
if ! id -u "$APP_USER" > /dev/null 2>&1; then
  log "Creando el usuario $APP_USER..."
  sudo adduser --system --group "$APP_USER"
fi

# Asegurarse de que el directorio de la aplicación existe
sudo mkdir -p "$APP_HOME"
sudo chown "$APP_USER":"$APP_USER" "$APP_HOME"

# 2. Detener los servicios existentes (si los hay)
log "Deteniendo los servicios existentes..."
# (Aquí se detendrían los servicios, por ejemplo, usando systemctl o Docker)
# Ejemplo con systemctl (si los servicios están gestionados con systemd):
# sudo systemctl stop alphapp-cloud-service.service

# 3. Desplegar la nueva versión
log "Desplegando la nueva versión..."

# Clonar o actualizar el código fuente desde el repositorio Git
log "Actualizando el código fuente desde Git..."
cd "$APP_HOME" || error "No se pudo acceder al directorio $APP_HOME"

# Asumiendo que el repositorio remoto es 'origin' y la rama es 'main'
sudo -u "$APP_USER" git pull origin main || error "Error al actualizar el código fuente desde Git"

# 4. Instalar dependencias (si es una aplicación Python)
log "Instalando dependencias..."
# (Si es una aplicación Python, instalar dependencias con pip)
if [ -f "requirements.txt" ]; then
  sudo -u "$APP_USER" pip install -r requirements.txt || error "Error al instalar las dependencias de Python"
fi

# 5. Aplicar migraciones de base de datos (si es necesario)
log "Aplicando migraciones de base de datos..."
# (Aquí se ejecutarían las migraciones de la base de datos, si las hay)
# Ejemplo con Django:
# sudo -u "$APP_USER" python manage.py migrate --settings=config.settings.$ENVIRONMENT || error "Error al aplicar las migraciones de la base de datos"

# 6. Recopilar archivos estáticos (si es una aplicación web)
log "Recopilando archivos estáticos..."
# (Si es una aplicación web, recopilar archivos estáticos)
# Ejemplo con Django:
# sudo -u "$APP_USER" python manage.py collectstatic --noinput --settings=config.settings.$ENVIRONMENT || error "Error al recopilar archivos estáticos"

# 7. Configurar los servicios
log "Configurando los servicios..."
# (Aquí se realizarían tareas de configuración específicas, como crear archivos de configuración)

# 8. Iniciar los servicios
log "Iniciando los servicios..."
# (Aquí se iniciarían los servicios, por ejemplo, usando systemctl o Docker)
# Ejemplo con systemctl (si los servicios están gestionados con systemd):
# sudo systemctl start alphapp-cloud-service.service

# 9. Ejecutar pruebas (opcional)
log "Ejecutando pruebas..."
# (Aquí se ejecutarían pruebas para verificar que el despliegue fue exitoso)
# Ejemplo con pytest:
# sudo -u "$APP_USER" pytest || log "Advertencia: Algunas pruebas fallaron, revisar los resultados"

log "Despliegue completado exitosamente."
exit 0
