#!/bin/bash
# Script para automatizar las tareas de respaldo en los servicios en la nube de Alphapp

# Variables de configuración (ajustar según necesidad)
BACKUP_DIR="/opt/alphapp/backups"      # Directorio donde se guardarán los backups
DATABASE_USER="alphapp_user"           # Usuario de la base de datos
DATABASE_PASSWORD="password123"        # Contraseña del usuario de la base de datos
DATABASE_NAME="alphapp_db"             # Nombre de la base de datos
CONFIG_FILES="/opt/alphapp/config/*.ini" # Archivos de configuración a respaldar
LOG_FILE="/var/log/alphapp/backup.log" # Archivo de registro
TIMESTAMP=$(date +%Y%m%d_%H%M%S)        # Marca de tiempo para los nombres de los archivos de backup

# Función para escribir en el archivo de registro
log() {
  echo "$(date +%Y-%m-%d\ %H:%M:%S) - $1" >> "$LOG_FILE"
}

# Función para respaldar la base de datos
backup_database() {
  log "Iniciando respaldo de la base de datos..."
  # Utilizar pg_dump para respaldar la base de datos PostgreSQL
  pg_dump -U "$DATABASE_USER" -d "$DATABASE_NAME" -f "$BACKUP_DIR/db_backup_$TIMESTAMP.sql" >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    log "Respaldo de la base de datos completado exitosamente."
  else
    log "Error al respaldar la base de datos."
    return 1
  fi
}

# Función para respaldar los archivos de configuración
backup_config_files() {
  log "Iniciando respaldo de los archivos de configuración..."
  # Crear un archivo tar.gz con los archivos de configuración
  tar -czvf "$BACKUP_DIR/config_backup_$TIMESTAMP.tar.gz" $CONFIG_FILES >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    log "Respaldo de los archivos de configuración completado exitosamente."
  else
    log "Error al respaldar los archivos de configuración."
    return 1
  fi
}

# Función principal para ejecutar las tareas de respaldo
main() {
  log "Iniciando el script de respaldo..."

  # Crear el directorio de backups si no existe
  mkdir -p "$BACKUP_DIR"

  # Ejecutar el respaldo de la base de datos
  backup_database

  # Ejecutar el respaldo de los archivos de configuración
  backup_config_files

  log "Script de respaldo finalizado."
}

# Ejecutar la función principal
main
