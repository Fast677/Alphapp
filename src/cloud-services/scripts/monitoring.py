#!/usr/bin/env python3
# Script para monitorear los servicios en la nube de Alphapp

import psutil
import time
import datetime
import os
import requests  # Para verificar la disponibilidad de la API
# Variables de configuración
LOG_FILE = "monitoring.log"
API_ENDPOINT = "https://api.alphapp.xyz/health"  # Reemplazar con el endpoint real de la API
# Funciones de utilidad
def log(message):
    """Escribe un mensaje en el archivo de registro."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def check_cpu_usage():
    """Verifica el uso de CPU."""
    cpu_usage = psutil.cpu_percent(interval=1)
    log(f"Uso de CPU: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    """Verifica el uso de memoria."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    log(f"Uso de memoria: {memory_usage}%")
    return memory_usage

def check_disk_usage(path="/"):
    """Verifica el uso de disco."""
    disk = psutil.disk_usage(path)
    disk_usage = disk.percent
    log(f"Uso de disco en {path}: {disk_usage}%")
    return disk_usage

def check_network_traffic():
    """Verifica el tráfico de red."""
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_received = net_io.bytes_recv
    log(f"Bytes enviados: {bytes_sent}, Bytes recibidos: {bytes_received}")
    return bytes_sent, bytes_received

def check_api_availability(url=API_ENDPOINT):
    """Verifica la disponibilidad de la API."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            log(f"API disponible en {url} (Código de estado: {response.status_code})")
            return True
        else:
            log(f"API no disponible en {url} (Código de estado: {response.status_code})")
            return False
    except requests.exceptions.RequestException as e:
        log(f"Error al verificar la API en {url}: {e}")
        return False

def main():
    """Función principal para ejecutar el monitoreo."""
    log("Iniciando el monitoreo de los servicios en la nube...")

    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_network_traffic()
        check_api_availability()

        time.sleep(60)  # Monitorea cada 60 segundos

if __name__ == "__main__":
    main()
