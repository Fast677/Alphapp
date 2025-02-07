import unittest
from django.test import TestCase
from src.backend.models.blog import Blog  # Ajusta la ruta según tu proyecto
from src.backend.models.user import User  # Ajusta la ruta según tu proyecto

class TestBlogModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="testpassword"
        )
        self.blog = Blog.objects.create(
            title="Test Blog Post",
            content="This is a test blog post",
            author=self.user
        )

    def test_blog_creation(self):
        self.assertIsNotNone(self.blog.id)
        self.assertEqual(self.blog.title, "Test Blog Post")
        self.assertEqual(self.blog.content, "This is a test blog post")
        self.assertEqual(self.blog.author, self.user)

    def test_blog_str_representation(self):
        self.assertEqual(str(self.blog), "Test Blog Post")

if __name__ == '__main__':
    unittest.main()
  
