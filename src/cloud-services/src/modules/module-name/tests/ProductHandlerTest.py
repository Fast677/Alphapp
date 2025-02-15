# cloud-services/src/modules/module-name/tests/ProductHandlerTest.py
import unittest
from unittest.mock import MagicMock
from src.modules.module_name.handlers.ProductHandler import ProductHandler
from src.modules.module_name.models.ProductModel import ProductModel

class TestProductHandler(unittest.TestCase):

    def setUp(self):
        self.database = MagicMock()
        self.product_handler = ProductHandler(self.database)

    def test_create_product(self):
        product_data = {
            'name': 'Test Product',
            'description': 'A test product',
            'price': 20.00
        }
        self.database.save.return_value = ProductModel(
            id=1,
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price']
        )
        new_product = self.product_handler.create_product(product_data)
        self.assertIsInstance(new_product, ProductModel)
        self.assertEqual(new_product.id, 1)
        self.assertEqual(new_product.name, product_data['name'])
        self.database.save.assert_called_once()

    def test_get_product_by_id(self):
        product_id = 1
        mock_product = ProductModel(
            id=product_id,
            name='Test Product',
            description='A test product',
            price=20.00
        )
        self.database.get_by_id.return_value = mock_product
        product = self.product_handler.get_product_by_id(product_id)
        self.assertIsInstance(product, ProductModel)
        self.assertEqual(product.id, product_id)
        self.database.get_by_id.assert_called_once_with('products', product_id)

    def test_update_product(self):
        product_id = 1
        product_data = {
            'name': 'Updated Product',
            'description': 'An updated product',
            'price': 25.00
        }
        mock_product = ProductModel(
            id=product_id,
            name='Test Product',
            description='A test product',
            price=20.00
        )
        self.database.get_by_id.return_value = mock_product
        self.database.update.return_value = ProductModel(
            id=product_id,
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price']
        )
        updated_product = self.product_handler.update_product(product_id, product_data)
        self.assertIsInstance(updated_product, ProductModel)
        self.assertEqual(updated_product.name, product_data['name'])
        self.database.get_by_id.assert_called_once_with('products', product_id)
        self.database.update.assert_called_once_with('products', product_id, product_data)

    def test_delete_product(self):
        product_id = 1
        self.database.delete.return_value = None
        self.product_handler.delete_product(product_id)
        self.database.delete.assert_called_once_with('products', product_id)

if __name__ == '__main__':
    unittest.main()
