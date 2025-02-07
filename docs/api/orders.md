# Recurso de Órdenes

Este recurso permite gestionar las órdenes de los usuarios.

## Lista de Órdenes
### `GET /orders`
Obtiene una lista de todas las órdenes.

**Parámetros:**
- `page` (opcional): Número de página para la paginación.
- `page_size` (opcional): Cantidad de elementos por página.

**Respuesta (JSON):**
```json
[
    {
        "id": 1,
        "user_id": 1,
        "order_date": "2024-07-26T15:00:00Z",
        "total": 50.00
    },
    {
        "id": 2,
        "user_id": 2,
        "order_date": "2024-07-25T10:00:00Z",
        "total": 100.00
    }
]
```

## Detalles de una Orden
### `GET /orders/{id}`
Obtiene los detalles de una orden específica.

**Parámetros:**
- `id` (obligatorio): ID de la orden.

**Respuesta (JSON):**
```json
{
    "id": 1,
    "user_id": 1,
    "order_date": "2024-07-26T15:00:00Z",
    "total": 50.00,
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        }
    ]
}
```

## Crear una Orden
### `POST /orders`
Crea una nueva orden.

**Cuerpo de la solicitud (JSON):**
```json
{
    "user_id": 1,
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        }
    ]
}
```

**Respuesta (JSON):**
```json
{
    "id": 3,
    "user_id": 1,
    "order_date": "2024-07-26T15:00:00Z",
    "total": 20.00,
    "items": [
        {
            "product_id": 1,
            "quantity": 2
        }
    ]
}
```

## Actualizar una Orden
### `PUT /orders/{id}`
Actualiza una orden existente.

**Parámetros:**
- `id` (obligatorio): ID de la orden.

**Cuerpo de la solicitud (JSON):**
```json
{
    "total": 120.00,
    "items": [
        {
            "product_id": 1,
            "quantity": 3
        }
    ]
}
```

**Respuesta (JSON):**
```json
{
    "id": 1,
    "user_id": 1,
    "order_date": "2024-07-26T15:00:00Z",
    "total": 120.00,
    "items": [
        {
            "product_id": 1,
            "quantity": 3
        }
    ]
}
```

## Borrar una Orden
### `DELETE /orders/{id}`
Borra una orden existente.

**Parámetros:**
- `id` (obligatorio): ID de la orden.

**Respuesta:**
Código HTTP: 204 No Content
```
