import unittest
import json
from your_app import app  # Reemplaza your_app con el nombre real de tu aplicación Flask/Django
from your_app.models import Post  # Reemplaza your_app.models con la ubicación real del modelo Post
# from models import Post
class TestPostRoutes(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.app = app.test_client()
        self.app.testing = True

    def test_create_post(self):
        """Prueba la creación de un nuevo post."""
        # Datos de prueba para crear un post
        post_data = {
            'title': 'Título de prueba',
            'content': 'Contenido de prueba',
            'author': 'usuario_de_prueba'
        }
        # Envía una solicitud POST a la ruta de creación de posts
        response = self.app.post(
            '/community/posts',  # Reemplaza con la ruta real
            data=json.dumps(post_data),
            content_type='application/json'
        )
        # Verifica que la respuesta sea exitosa (código 201 Created)
        self.assertEqual(response.status_code, 201)
        # Verifica que la respuesta contenga los datos del nuevo post
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['title'], post_data['title'])
        self.assertEqual(data['content'], post_data['content'])
        self.assertEqual(data['author'], post_data['author'])

    def test_create_post_invalid_data(self):
        """Prueba la creación de un post con datos inválidos."""
        # Datos de prueba incompletos
        post_data = {
            'content': 'Contenido de prueba'
        }

        # Envía una solicitud POST con datos inválidos
        response = self.app.post(
            '/community/posts',  # Reemplaza con la ruta real
            data=json.dumps(post_data),
            content_type='application/json'
        )

        # Verifica que la respuesta sea un error (código 400 Bad Request)
        self.assertEqual(response.status_code, 400)

    def test_get_all_posts(self):
        """Prueba la obtención de todos los posts."""
        # Crea algunos posts de prueba (opcional, si la base de datos está vacía)
        # Envía una solicitud GET a la ruta para obtener todos los posts
        response = self.app.get('/community/posts')  # Reemplaza con la ruta real
        # Verifica que la respuesta sea exitosa (código 200 OK)
        self.assertEqual(response.status_code, 200)
        # Verifica que la respuesta contenga una lista de posts (o una lista vacía)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
