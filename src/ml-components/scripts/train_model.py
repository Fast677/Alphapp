import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import logging

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

def preprocess_data(df, target_column):
    """Preprocesa los datos para el entrenamiento del modelo.

    Args:
        df (pandas.DataFrame): DataFrame con los datos.
        target_column (str): Nombre de la columna objetivo.

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
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Escalar características numéricas
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        logging.info("Datos preprocesados y escalados correctamente.")
        return X_train_scaled, X_test_scaled, y_train
    except Exception as e:
        logging.error(f"Error al preprocesar datos: {e}")
        return None, None, None

def build_model(input_shape):
    """Crea un modelo de TensorFlow.

    Args:
        input_shape (int): Forma de la entrada de datos.

    Returns:
        tensorflow.keras.models.Sequential: Modelo de TensorFlow.
    """
    try:
        logging.info("Construyendo modelo...")
        model = tf.keras.models.Sequential([
            tf.keras.layers.Input(shape=(input_shape,)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')  # Ejemplo de clasificación binaria
        ])
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        logging.info("Modelo construido y compilado correctamente.")
        return model
    except Exception as e:
         logging.error(f"Error al construir el modelo: {e}")
         return None

def train_model(model, X_train, y_train, epochs=100, batch_size=32):
    """Entrena el modelo de TensorFlow.

    Args:
        model (tensorflow.keras.models.Sequential): Modelo de TensorFlow.
        X_train (numpy.ndarray): Datos de entrenamiento escalados.
        y_train (numpy.ndarray): Vector objetivo de entrenamiento.
        epochs (int): Número de épocas de entrenamiento.
        batch_size (int): Tamaño del lote.
    """
    if model is None or X_train is None or y_train is None:
         logging.error("No se puede entrenar el modelo debido a datos inválidos.")
         return
    try:
        logging.info("Entrenando modelo...")
        model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=2)
        logging.info("Modelo entrenado correctamente.")
    except Exception as e:
        logging.error(f"Error al entrenar el modelo: {e}")

def save_model(model, model_path):
    """Guarda el modelo entrenado en formato SavedModel.

    Args:
        model (tensorflow.keras.models.Sequential): Modelo de TensorFlow entrenado.
        model_path (str): Ruta donde se guardará el modelo.
    """
    if model is None:
        logging.error("No se puede guardar el modelo debido a que es inválido.")
        return
    try:
        logging.info(f"Guardando modelo en {model_path}")
        model.save(model_path)
        logging.info("Modelo guardado correctamente.")
    except Exception as e:
        logging.error(f"Error al guardar el modelo: {e}")


def main():
    """Función principal para entrenar el modelo."""
    # Definir rutas y configuraciones
    data_dir = 'data/training_data'
    model_dir = 'models/my_model'
    target_column = 'target'  # Nombre de la columna objetivo en tus datos

    # Asegurar que el directorio del modelo existe
    os.makedirs(model_dir, exist_ok=True)

    # Buscar el archivo de datos en el directorio data
    data_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

    if not data_files:
        logging.error(f"No se encontraron archivos CSV en el directorio {data_dir}")
        return

    data_file = os.path.join(data_dir, data_files)  # Tomar el primer archivo CSV encontrado

    # Cargar y preprocesar datos
    df = load_data(data_file)
    X_train, X_test, y_train = preprocess_data(df, target_column)

    if X_train is None or X_test is None or y_train is None:
        logging.error("No se pudo continuar debido a errores en la carga o preprocesamiento de datos.")
        return

    # Construir modelo
    input_shape = X_train.shape[1]  # Obtener el número de características
    model = build_model(input_shape)
    if model is None:
        logging.error("No se pudo continuar debido a errores en la construcción del modelo.")
        return

    # Entrenar modelo
    train_model(model, X_train, y_train)

    # Guardar modelo
    save_model(model, model_dir)

    logging.info("Proceso de entrenamiento del modelo completado.")

if __name__ == "__main__":
    main()
