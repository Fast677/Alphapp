import unittest
from django.test import TestCase
from src.backend.models.order import Order  # Ajusta la ruta según tu proyecto
from src.backend.models.user import User  # Ajusta la ruta según tu proyecto
from src.backend.models.product import Product  # Ajusta la ruta según tu proyecto

class TestOrderModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="testpassword"
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=19.99
        )
        self.order = Order.objects.create(
            user=self.user,
            total=19.99
        )
        self.order.products.add(self.product)

    def test_order_creation(self):
        self.assertIsNotNone(self.order.id)
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.total, 19.99)

    def test_order_str_representation(self):
        self.assertEqual(str(self.order), f"Order {self.order.id}")

if __name__ == '__main__':
    unittest.main()
  
