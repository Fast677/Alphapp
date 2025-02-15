#!/bin/bash
# Script para automatizar las tareas de restauración en los servicios en la nube de Alphapp

# Variables de configuración (ajustar según necesidad)
BACKUP_DIR="/opt/alphapp/backups"      # Directorio donde se guardan los backups
DATABASE_USER="alphapp_user"           # Usuario de la base de datos
DATABASE_PASSWORD="password123"        # Contraseña del usuario de la base de datos
DATABASE_NAME="alphapp_db"             # Nombre de la base de datos
CONFIG_FILES="/opt/alphapp/config/*.ini" # Archivos de configuración a restaurar
LOG_FILE="/var/log/alphapp/restore.log" # Archivo de registro
BACKUP_FILE=""                         # Archivo de backup a restaurar (se debe especificar)

# Función para escribir en el archivo de registro
log() {
  echo "$(date +%Y-%m-%d %H:%M:%S) - $1" >> "$LOG_FILE"
}

# Función para restaurar la base de datos
restore_database() {
  log "Iniciando restauración de la base de datos..."
  if [ -z "$BACKUP_FILE" ]; then
    log "Error: No se ha especificado el archivo de backup para la base de datos."
    return 1
  fi
  # Utilizar psql para restaurar la base de datos PostgreSQL
  psql -U "$DATABASE_USER" -d "$DATABASE_NAME" -f "$BACKUP_FILE" >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    log "Restauración de la base de datos completada exitosamente."
  else
    log "Error al restaurar la base de datos."
    return 1
  fi
}

# Función para restaurar los archivos de configuración
restore_config_files() {
  log "Iniciando restauración de los archivos de configuración..."
  if [ -z "$BACKUP_FILE" ]; then
    log "Error: No se ha especificado el archivo de backup para los archivos de configuración."
    return 1
  fi
  # Descomprimir el archivo tar.gz con los archivos de configuración
  tar -xzvf "$BACKUP_FILE" -C /opt/alphapp/config/ >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    log "Restauración de los archivos de configuración completada exitosamente."
  else
    log "Error al restaurar los archivos de configuración."
    return 1
  fi
}

# Función principal para ejecutar las tareas de restauración
main() {
  log "Iniciando el script de restauración..."

  # Verificar que se haya especificado el archivo de backup
  if [ -z "$BACKUP_FILE" ]; then
    log "Error: Debe especificar el archivo de backup a restaurar usando la variable BACKUP_FILE."
    exit 1
  fi

  # Ejecutar la restauración de la base de datos
  restore_database

  # Ejecutar la restauración de los archivos de configuración
  restore_config_files

  log "Script de restauración finalizado."
}

# Ejecutar la función principal
main
