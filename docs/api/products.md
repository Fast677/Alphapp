# Recurso de Productos

Este recurso permite gestionar los productos de la tienda.

## Lista de Productos
### `GET /products`
Obtiene una lista de todos los productos.

**Parámetros:**
- `page` (opcional): Número de página para la paginación.
- `page_size` (opcional): Cantidad de elementos por página.

**Respuesta (JSON):**
```json
[
    {
        "id": 1,
        "name": "Product 1",
        "description": "Description of product 1",
        "price": 10.00
    },
    {
        "id": 2,
        "name": "Product 2",
        "description": "Description of product 2",
        "price": 20.00
    }
]
```

## Detalles de un Producto
### `GET /products/{id}`
Obtiene los detalles de un producto específico.

**Parámetros:**
- `id` (obligatorio): ID del producto.

**Respuesta (JSON):**
```json
{
    "id": 1,
    "name": "Product 1",
    "description": "Description of product 1",
    "price": 10.00
}
```

## Crear un Producto
### `POST /products`
Crea un nuevo producto.

**Cuerpo de la solicitud (JSON):**
```json
{
    "name": "New Product",
    "description": "Description of new product",
    "price": 15.00
}
```

**Respuesta (JSON):**
```json
{
    "id": 3,
    "name": "New Product",
    "description": "Description of new product",
    "price": 15.00
}
```

## Actualizar un Producto
### `PUT /products/{id}`
Actualiza un producto existente.

**Parámetros:**
- `id` (obligatorio): ID del producto.

**Cuerpo de la solicitud (JSON):**
```json
{
    "name": "Updated Product",
    "description": "Updated description",
    "price": 12.00
}
```

**Respuesta (JSON):**
```json
{
    "id": 1,
    "name": "Updated Product",
    "description": "Updated description",
    "price": 12.00
}
```

## Borrar un Producto
### `DELETE /products/{id}`
Borra un producto existente.

**Parámetros:**
- `id` (obligatorio): ID del producto.

**Respuesta:**
Código HTTP: 204 No Content
```

Este archivo documenta los diferentes endpoints relacionados con los productos, proporcionando ejemplos de solicitudes y respuestas, así como los parámetros que cada uno requiere.
