import unittest
from django.test import TestCase
from src.backend.models.product import Product  # Ajusta la ruta según tu proyecto

class TestProductModel(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=19.99
        )

    def test_product_creation(self):
        self.assertIsNotNone(self.product.id)
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "This is a test product")
        self.assertEqual(self.product.price, 19.99)

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), "Test Product")

if __name__ == '__main__':
    unittest.main()
  
