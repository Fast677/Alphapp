import unittest
from django.test import TestCase
from src.backend.models.user import User  # Ajusta la ruta según tu proyecto

class TestUserModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="testpassword"
        )

    def test_user_creation(self):
        self.assertIsNotNone(self.user.id)
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), "testuser")

if __name__ == '__main__':
    unittest.main()
