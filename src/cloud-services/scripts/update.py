#!/usr/bin/env python3
# Script para automatizar las tareas de actualización en los servicios en la nube de Alphapp

import os
import subprocess
import logging

# Configuración básica del logging
logging.basicConfig(filename='/var/log/alphapp/update.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Variables de configuración (ajustar según necesidad)
APP_DIR = "/opt/alphapp"  # Directorio de la aplicación
VENV_DIR = os.path.join(APP_DIR, "venv") # directorio del entorno virtual
REQUIREMENTS_FILE = os.path.join(APP_DIR, "requirements.txt") # Archivo de dependencias
BACKUP_SCRIPT = os.path.join(APP_DIR, "scripts", "backup.sh") # Script de respaldo
RESTORE_SCRIPT = os.path.join(APP_DIR, "scripts", "restore.sh") # Script de restauración

def log(message, level=logging.INFO):
    """Escribe un mensaje en el archivo de registro."""
    logging.log(level, message)

def run_command(command, check=True):
    """Ejecuta un comando en la línea de comandos y registra la salida."""
    log(f"Ejecutando comando: {' '.join(command)}")
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=check)
        log(f"Salida: {result.stdout}")
        if result.stderr:
            log(f"Error: {result.stderr}", level=logging.ERROR)
        return result
    except subprocess.CalledProcessError as e:
        log(f"Error al ejecutar el comando: {e}", level=logging.ERROR)
        raise

def create_virtualenv():
    """Crea un entorno virtual para la aplicación."""
    log("Creando entorno virtual...")
    try:
        run_command(["python3", "-m", "venv", VENV_DIR])
        log("Entorno virtual creado exitosamente.")
    except Exception as e:
        log(f"Error al crear el entorno virtual: {e}", level=logging.ERROR)
        raise

def install_dependencies():
    """Instala las dependencias de Python desde el archivo requirements.txt."""
    log("Instalando dependencias...")
    try:
        run_command([os.path.join(VENV_DIR, "bin", "pip"), "install", "-r", REQUIREMENTS_FILE])
        log("Dependencias instaladas exitosamente.")
    except Exception as e:
        log(f"Error al instalar las dependencias: {e}", level=logging.ERROR)
        raise

def backup_data():
    """Realiza un respaldo de los datos antes de la actualización."""
    log("Realizando respaldo de los datos...")
    try:
        run_command(["bash", BACKUP_SCRIPT])
        log("Respaldo de los datos completado exitosamente.")
    except Exception as e:
        log(f"Error al realizar el respaldo de los datos: {e}", level=logging.ERROR)
        raise

def restore_data():
    """Restaura los datos en caso de que la actualización falle."""
    log("Restaurando los datos...")
    try:
        run_command(["bash", RESTORE_SCRIPT])
        log("Restauración de los datos completada exitosamente.")
    except Exception as e:
        log(f"Error al restaurar los datos: {e}", level=logging.ERROR)
        raise

def update_source_code():
    """Actualiza el código fuente desde el repositorio (ejemplo con git)."""
    log("Actualizando el código fuente...")
    try:
        run_command(["git", "pull", "origin", "main"])  # Ajustar según la rama
        log("Código fuente actualizado exitosamente.")
    except Exception as e:
        log(f"Error al actualizar el código fuente: {e}", level=logging.ERROR)
        raise

def migrate_database():
    """Ejecuta las migraciones de la base de datos (ejemplo con Django)."""
    log("Ejecutando migraciones de la base de datos...")
    try:
        run_command([os.path.join(VENV_DIR, "bin", "python"), "manage.py", "migrate"])  # Ajustar según el framework
        log("Migraciones de la base de datos completadas exitosamente.")
    except Exception as e:
        log(f"Error al ejecutar las migraciones de la base de datos: {e}", level=logging.ERROR)
        raise

def main():
    """Función principal para ejecutar las tareas de actualización."""
    log("Iniciando el script de actualización...")

    try:
        # 1. Realizar un respaldo de los datos
        backup_data()

        # 2. Actualizar el código fuente
        update_source_code()

        # 3. Instalar o actualizar las dependencias
        if not os.path.exists(VENV_DIR):
            create_virtualenv()
        install_dependencies()

        # 4. Ejecutar las migraciones de la base de datos
        migrate_database()

        log("Script de actualización finalizado exitosamente.")

    except Exception as e:
        log(f"Error durante la actualización: {e}", level=logging.ERROR)
        log("Intentando restaurar los datos...", level=logging.WARNING)
        try:
            restore_data()
            log("Restauración completada.", level=logging.INFO)
        except Exception as restore_error:
            log(f"Error durante la restauración: {restore_error}", level=logging.ERROR)
            log("La restauración falló. Revise los logs y realice la restauración manualmente.", level=logging.CRITICAL)
        finally:
            exit(1)

if __name__ == "__main__":
    main()
