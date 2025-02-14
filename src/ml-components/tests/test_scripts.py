import unittest
import os
import pandas as pd
# Asegurarse de que el path es correcto, ajustarlo segun la estructura real
from ml_components.scripts import data_processing, train_model, infer_model

class TestScripts(unittest.TestCase):
    # Prepara el ambiente de prueba
    def setUp(self):
        self.test_data_path = 'ml_components/data/test_data.csv'
        self.test_model_path = 'ml_components/models/test_model'
        # Crea datos de prueba para usar en los tests
        test_df = pd.DataFrame({
            'feature1': [1-3],
            'feature2': [4-6],
            'target': [1]
        })
        test_df.to_csv(self.test_data_path, index=False)
        # Crea un archivo dummy para el modelo
        os.makedirs(os.path.dirname(self.test_model_path), exist_ok=True)
        with open(self.test_model_path, 'w') as f:
            f.write("Dummy model file")

    # Limpia el ambiente de prueba
    def tearDown(self):
        os.remove(self.test_data_path)
        os.remove(self.test_model_path)
    
    def test_data_processing(self):
        # Crea un objeto DataProcessor
        processor = data_processing.DataProcessor()
        # Prueba el procesamiento de datos
        processed_df = processor.process_data(self.test_data_path)
        # Verifica que el resultado no sea nulo
        self.assertIsNotNone(processed_df)
        # Verifica que el tipo de dato sea el correcto
        self.assertIsInstance(processed_df, pd.DataFrame)
        # Verificar que la salida tenga la estructura esperada
        self.assertIn('feature1', processed_df.columns)
        self.assertIn('feature2', processed_df.columns)
        self.assertIn('target', processed_df.columns)
        
    def test_train_model(self):
        # Crea un objeto ModelTrainer
        trainer = train_model.ModelTrainer()
        # Prueba el entrenamiento del modelo
        model_path = trainer.train_model(self.test_data_path,self.test_model_path)
        # Verifica que el resultado no sea nulo
        self.assertIsNotNone(model_path)
        # Verifica si el modelo se guardó correctamente
        self.assertTrue(os.path.exists(model_path))
    
    def test_infer_model(self):
       # Crea un objeto ModelInferencer
       inferencer = infer_model.ModelInferencer()
       # Prueba la inferencia del modelo
       predictions = inferencer.infer_model(self.test_model_path, self.test_data_path)
       # Verifica que el resultado no sea nulo
       self.assertIsNotNone(predictions)
       # Verifica que el resultado sea una lista
       self.assertIsInstance(predictions, list)
    
if __name__ == '__main__':
    unittest.main()
