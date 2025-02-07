# Documentación de la API de Alphapp

Esta documentación proporciona información sobre cómo interactuar con la API de Alphapp.

## Autenticación
Todas las solicitudes a la API requieren autenticación mediante tokens JWT. Para obtener un token, realiza una solicitud POST a `/auth/login` con tu usuario y contraseña.

## Convenciones de Nombres
- Los endpoints usan nombres en plural (por ejemplo, `/users` para usuarios, `/products` para productos).
- Se usan códigos HTTP estándar para las respuestas (200 OK, 201 Created, 400 Bad Request, etc.).
- Los datos se intercambian en formato JSON.

## Recursos
A continuación, se detallan los recursos disponibles en la API:
- [Usuarios](users.md)
- [Productos](products.md)
- [Órdenes](orders.md)
- [Blog](blog.md)
