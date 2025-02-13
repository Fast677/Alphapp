import pandas as pd
import logging
import os
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_data(data_path):
    """Carga datos desde un archivo CSV usando Pandas.

    Args:
        data_path (str): Ruta al archivo CSV.

    Returns:
        pandas.DataFrame: DataFrame con los datos cargados.
    """
    try:
        logging.info(f"Cargando datos desde {data_path}")
        df = pd.read_csv(data_path)
        logging.info(f"Datos cargados correctamente: {df.shape}")
        return df
    except FileNotFoundError:
        logging.error(f"Error: No se encontró el archivo {data_path}")
        return None
    except Exception as e:
        logging.error(f"Error al cargar datos: {e}")
        return None


def preprocess_data(df, target_column, test_size=0.2, random_state=42):
    """Preprocesa los datos para el entrenamiento del modelo.

    Args:
        df (pandas.DataFrame): DataFrame con los datos.
        target_column (str): Nombre de la columna objetivo.
        test_size (float): Proporción de datos para el conjunto de prueba.
        random_state (int): Semilla para la división de datos.

    Returns:
        tuple: Tupla con los datos de entrenamiento y prueba escalados, y el vector objetivo.
    """
    if df is None:
        return None, None, None

    try:
        logging.info("Preprocesando datos...")
        # Separar características y objetivo
        X = df.drop(target_column, axis=1)
        y = df[target_column]

        # Dividir datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)


        # Escalar características numéricas
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        logging.info("Datos preprocesados y escalados correctamente.")
        return X_train_scaled, X_test_scaled, y_train, y_test
    except Exception as e:
        logging.error(f"Error al preprocesar datos: {e}")
        return None, None, None, None


def save_config(config, config_path):
    """Guarda un diccionario de configuración en un archivo JSON.

    Args:
        config (dict): Diccionario con la configuración.
        config_path (str): Ruta donde se guardará el archivo JSON.
    """
    try:
        logging.info(f"Guardando configuración en {config_path}")
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
        logging.info("Configuración guardada correctamente.")
    except Exception as e:
        logging.error(f"Error al guardar la configuración: {e}")


def load_config(config_path):
    """Carga un diccionario de configuración desde un archivo JSON.

    Args:
        config_path (str): Ruta al archivo JSON.

    Returns:
        dict: Diccionario con la configuración cargada.
    """
    try:
        logging.info(f"Cargando configuración desde {config_path}")
        with open(config_path, 'r') as f:
            config = json.load(f)
        logging.info("Configuración cargada correctamente.")
        return config
    except FileNotFoundError:
         logging.error(f"Error: No se encontró el archivo de configuración {config_path}")
         return None
    except Exception as e:
        logging.error(f"Error al cargar la configuración: {e}")
        return None


def ensure_directory_exists(directory_path):
    """Verifica si un directorio existe y, si no, lo crea.

    Args:
         directory_path (str): Ruta del directorio a verificar.
    """
    try:
        if not os.path.exists(directory_path):
            logging.info(f"Creando directorio {directory_path}")
            os.makedirs(directory_path)
        logging.info(f"Directorio {directory_path} listo.")
    except Exception as e:
         logging.error(f"Error al crear el directorio: {e}")


if __name__ == '__main__':
    # Ejemplo de uso de las funciones
    # Crear un directorio de prueba
    test_dir = 'test_utils_dir'
    ensure_directory_exists(test_dir)

    # Ejemplo de uso de save_config y load_config
    config_data = {
        "model_name": "my_model",
        "epochs": 100,
        "batch_size": 32,
        "learning_rate": 0.001
    }
    config_file = os.path.join(test_dir, 'config.json')
    save_config(config_data, config_file)
    loaded_config = load_config(config_file)

    if loaded_config:
        print("Configuración cargada:", loaded_config)

    # Ejemplo de uso de load_data
    # Crear un archivo CSV de prueba
    test_csv = os.path.join(test_dir, 'test_data.csv')
    test_df = pd.DataFrame({'feature1': [1-5], 'feature2': [6-10], 'target': [1, 1]})
    test_df.to_csv(test_csv, index=False)
    loaded_df = load_data(test_csv)

    if loaded_df is not None:
        print("\nDatos cargados:")
        print(loaded_df.head())

         # Ejemplo de uso de preprocess_data
        X_train, X_test, y_train, y_test = preprocess_data(loaded_df, 'target')
        if X_train is not None and X_test is not None and y_train is not None:
            print("\nForma de los datos de entrenamiento:", X_train.shape)
            print("Forma del vector objetivo de entrenamiento:", y_train.shape)
            print("Forma de los datos de prueba:", X_test.shape)
            print("Forma del vector objetivo de prueba:", y_test.shape)


    # Limpieza del directorio de prueba
    os.remove(test_csv)
    os.remove(config_file)
    os.rmdir(test_dir)

    print("\nEjemplos completados.")
