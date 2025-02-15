# cloud-services/src/modules/module-name/handlers/ProductHandler.py
from flask import Flask, request, jsonify
# Suponiendo que tienes un servicio para manejar la lógica de productos
from . import product_service

# Importa las dependencias necesarias, como Flask y cualquier servicio relacionado con productos

class ProductHandler:
    def __init__(self, product_service):
        self.product_service = product_service

    def create_product(self):
        data = request.get_json()
        try:
            new_product = self.product_service.create_product(data)
            return jsonify(new_product), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_product(self, product_id):
        try:
            product = self.product_service.get_product(product_id)
            if product:
                return jsonify(product), 200
            return jsonify({'message': 'Producto no encontrado'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_product(self, product_id):
        data = request.get_json()
        try:
            updated_product = self.product_service.update_product(product_id, data)
            if updated_product:
                return jsonify(updated_product), 200
            return jsonify({'message': 'Producto no encontrado'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_product(self, product_id):
        try:
            if self.product_service.delete_product(product_id):
                return '', 204
            return jsonify({'message': 'Producto no encontrado'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Ejemplo de uso dentro de una aplicación Flask
app = Flask(__name__)
product_handler = ProductHandler(product_service)

@app.route('/products', methods=['POST'])
def create_product():
    return product_handler.create_product()

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return product_handler.get_product(product_id)

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return product_handler.update_product(product_id)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return product_handler.delete_product(product_id)

if __name__ == '__main__':
    app.run(debug=True)
