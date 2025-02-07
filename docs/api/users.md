# Recurso de Usuarios

Este recurso permite gestionar los usuarios de la plataforma.

## Lista de Usuarios
### `GET /users`
Obtiene una lista de todos los usuarios.

**Parámetros:**
- `page` (opcional): Número de página para la paginación.
- `page_size` (opcional): Cantidad de elementos por página.

**Respuesta (JSON):**
```json
[
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com"
    },
    {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com"
    }
]
```

## Detalles de un Usuario
### `GET /users/{id}`
Obtiene los detalles de un usuario específico.

**Parámetros:**
- `id` (obligatorio): ID del usuario.

**Respuesta (JSON):**
```json
{
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "date_joined": "2024-07-26T15:00:00Z"
}
```

## Crear un Usuario
### `POST /users`
Crea un nuevo usuario.

**Cuerpo de la solicitud (JSON):**
```json
{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "password"
}
```

**Respuesta (JSON):**
```json
{
    "id": 3,
    "username": "newuser",
    "email": "newuser@example.com",
    "date_joined": "2024-07-26T15:00:00Z"
}
```

## Actualizar un Usuario
### `PUT /users/{id}`
Actualiza un usuario existente.

**Parámetros:**
- `id` (obligatorio): ID del usuario.

**Cuerpo de la solicitud (JSON):**
```json
{
    "username": "updateduser",
    "email": "updateduser@example.com"
}
```

**Respuesta (JSON):**
```json
{
    "id": 1,
    "username": "updateduser",
    "email": "updateduser@example.com",
    "date_joined": "2024-07-26T15:00:00Z"
}
```

## Borrar un Usuario
### `DELETE /users/{id}`
Borra un usuario existente.

**Parámetros:**
- `id` (obligatorio): ID del usuario.

**Respuesta:**
Código HTTP: 204 No Content
```

Este archivo documenta los diferentes endpoints relacionados con los usuarios, proporcionando ejemplos de solicitudes y respuestas, así como los parámetros que cada uno requiere.
