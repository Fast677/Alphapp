# Recurso de Blogs

Este recurso permite gestionar las entradas del blog.

## Lista de Blogs
### `GET /blogs`
Obtiene una lista de todas las entradas del blog.

**Parámetros:**
- `page` (opcional): Número de página para la paginación.
- `page_size` (opcional): Cantidad de elementos por página.

**Respuesta (JSON):**
```json
[
    {
        "id": 1,
        "title": "Primer Blog",
        "content": "Contenido del primer blog",
        "author": "Autor 1",
        "created_at": "2024-07-26T15:00:00Z"
    },
    {
        "id": 2,
        "title": "Segundo Blog",
        "content": "Contenido del segundo blog",
        "author": "Autor 2",
        "created_at": "2024-07-25T10:00:00Z"
    }
]
```

## Detalles de una Entrada del Blog
### `GET /blogs/{id}`
Obtiene los detalles de una entrada específica del blog.

**Parámetros:**
- `id` (obligatorio): ID de la entrada del blog.

**Respuesta (JSON):**
```json
{
    "id": 1,
    "title": "Primer Blog",
    "content": "Contenido del primer blog",
    "author": "Autor 1",
    "created_at": "2024-07-26T15:00:00Z"
}
```

## Crear una Entrada del Blog
### `POST /blogs`
Crea una nueva entrada del blog.

**Cuerpo de la solicitud (JSON):**
```json
{
    "title": "Nuevo Blog",
    "content": "Contenido del nuevo blog",
    "author": "Autor 3"
}
```

**Respuesta (JSON):**
```json
{
    "id": 3,
    "title": "Nuevo Blog",
    "content": "Contenido del nuevo blog",
    "author": "Autor 3",
    "created_at": "2024-07-26T15:00:00Z"
}
```

## Actualizar una Entrada del Blog
### `PUT /blogs/{id}`
Actualiza una entrada existente del blog.

**Parámetros:**
- `id` (obligatorio): ID de la entrada del blog.

**Cuerpo de la solicitud (JSON):**
```json
{
    "title": "Blog Actualizado",
    "content": "Contenido actualizado",
    "author": "Autor 3"
}
```

**Respuesta (JSON):**
```json
{
    "id": 1,
    "title": "Blog Actualizado",
    "content": "Contenido actualizado",
    "author": "Autor 3",
    "created_at": "2024-07-26T15:00:00Z"
}
```

## Borrar una Entrada del Blog
### `DELETE /blogs/{id}`
Borra una entrada existente del blog.

**Parámetros:**
- `id` (obligatorio): ID de la entrada del blog.

**Respuesta:**
Código HTTP: 204 No Content
```

Este archivo documenta los diferentes endpoints relacionados con las entradas del blog, proporcionando ejemplos de solicitudes y respuestas, así como los parámetros que cada uno requiere.
