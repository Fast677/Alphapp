# Casos de Uso Comunes de la API de Servicios en la Nube

Esta sección describe los casos de uso más comunes de la API de servicios en la nube de Alphapp, proporcionando ejemplos y guías paso a paso para facilitar su integración.

## 1. Crear un Nuevo Usuario

Para crear un nuevo usuario, se debe enviar una solicitud `POST` a la ruta `/users` con los datos del usuario en formato JSON.

**Ejemplo de Solicitud:**

```json
{
  "username": "nuevoUsuario",
  "email": "nuevo.usuario@example.com",
  "password": "ContraseñaSegura123",
  "firstName": "Nuevo",
  "lastName": "Usuario"
}
```

**Ejemplo de Respuesta Exitosa (Código 201 Created):**

```json
{
  "id": 123,
  "username": "nuevoUsuario",
  "email": "nuevo.usuario@example.com",
  "firstName": "Nuevo",
  "lastName": "Usuario",
  "profileImage": null,
  "createdAt": "2024-07-26T10:00:00Z",
  "updatedAt": "2024-07-26T10:00:00Z"
}
```

**Nota:** Asegúrese de incluir todos los campos obligatorios en la solicitud. Consulte la documentación de la API para obtener más detalles sobre los campos y sus requisitos.

## 2. Obtener Información de un Usuario

Para obtener la información de un usuario específico, se debe enviar una solicitud `GET` a la ruta `/users/{id}`, donde `{id}` es el ID del usuario.

**Ejemplo de Solicitud:**

```
GET /users/123
```

**Ejemplo de Respuesta Exitosa (Código 200 OK):**

```json
{
  "id": 123,
  "username": "usuarioEjemplo",
  "email": "usuario.ejemplo@example.com",
  "firstName": "Ejemplo",
  "lastName": "Usuario",
  "profileImage": "https://example.com/imagen.jpg",
  "createdAt": "2024-07-26T10:00:00Z",
  "updatedAt": "2024-07-26T12:30:00Z"
}
```

**Nota:** Si el usuario no existe, la API devolverá un código de error 404 Not Found.

## 3. Actualizar la Información de un Usuario

Para actualizar la información de un usuario, se debe enviar una solicitud `PUT` o `PATCH` a la ruta `/users/{id}`, donde `{id}` es el ID del usuario, con los datos a actualizar en formato JSON.

**Ejemplo de Solicitud (PATCH):**

```json
{
  "firstName": "NuevoNombre",
  "lastName": "NuevoApellido"
}
```

**Ejemplo de Respuesta Exitosa (Código 200 OK):**

```json
{
  "id": 123,
  "username": "usuarioEjemplo",
  "email": "usuario.ejemplo@example.com",
  "firstName": "NuevoNombre",
  "lastName": "NuevoApellido",
  "profileImage": "https://example.com/imagen.jpg",
  "createdAt": "2024-07-26T10:00:00Z",
  "updatedAt": "2024-07-27T08:00:00Z"
}
```

**Nota:** Utilice `PUT` para reemplazar todos los campos del usuario y `PATCH` para actualizar solo los campos especificados.

## 4. Eliminar un Usuario

Para eliminar un usuario, se debe enviar una solicitud `DELETE` a la ruta `/users/{id}`, donde `{id}` es el ID del usuario.

**Ejemplo de Solicitud:**

```
DELETE /users/123
```

**Ejemplo de Respuesta Exitosa (Código 204 No Content):**

```
(Sin cuerpo de respuesta)
```

**Nota:** La eliminación de un usuario es una operación irreversible. Asegúrese de tener la confirmación del usuario antes de realizar esta acción.

## 5. Autenticación de Usuario

La API utiliza autenticación basada en tokens JWT (JSON Web Tokens). Para autenticarse, se debe enviar una solicitud `POST` a la ruta `/auth/login` con las credenciales del usuario.

**Ejemplo de Solicitud:**

```json
{
  "username": "usuarioEjemplo",
  "password": "ContraseñaSegura123"
}
```

**Ejemplo de Respuesta Exitosa (Código 200 OK):**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

**Nota:** El token JWT debe incluirse en el encabezado `Authorization` de todas las solicitudes posteriores como `Bearer <token>`.


### Explicación del código:

*   **Estructura del documento:**
    *   El documento está escrito en **Markdown**, lo que facilita su lectura y edición.
    *   Utiliza encabezados (`#`, `##`) para estructurar el contenido en secciones lógicas.
    *   Incluye **ejemplos de código en formato JSON** para mostrar la estructura de las solicitudes y respuestas de la API.
    *   Utiliza **bloques de código** (` ```json`) para resaltar los ejemplos de código.
    *   Incluye **notas y explicaciones adicionales** para aclarar conceptos y proporcionar información importante.
*   **Casos de uso:**
    *   Describe los **casos de uso más comunes** de la API, como crear, obtener, actualizar y eliminar usuarios.
    *   Proporciona **ejemplos completos** de solicitudes y respuestas para cada caso de uso.
    *   Incluye **información sobre los códigos de estado HTTP** que se devuelven en cada caso.
*   **Autenticación:**
    *   Describe el **proceso de autenticación** utilizando tokens JWT.
    *   Proporciona un ejemplo de cómo obtener un token JWT y cómo incluirlo en las solicitudes.

### Consideraciones adicionales:

*   Este es solo un ejemplo básico. Dependiendo de los requisitos de la API de Alphapp, el archivo podría incluir casos de uso adicionales, como:
    *   **Gestión de roles y permisos**.
    *   **Recuperación de contraseñas**.
    *   **Validación de datos**.
    *   **Integración con otros servicios**.

*   Es importante que los ejemplos de código sean **válidos y representativos** de los datos que se envían y se reciben a través de la API.
*   Este archivo Markdown sirve como **documentación para los desarrolladores** que utilizarán la API, mostrándoles cómo realizar las tareas más comunes.
*   Los ejemplos deben reflejar todos los campos definidos en el esquema (`user.js`) y deben ser coherentes con los ejemplos de solicitudes y respuestas en formato JSON (`create_user_request.json`, `get_user_response.json`).
*   La correcta definición de los casos de uso es fundamental para la **integración con la plataforma central** (`alphapp.xyz`) a través de la API. También promueve la **modularidad** dentro de la estructura de carpetas.
*   Este archivo de documentación ayuda a asegurar que la API se utilice correctamente y cumple con los requisitos de la plataforma Alphapp, facilitando el **desarrollo de aplicaciones y servicios**.
*   Es importante considerar las **pruebas de seguridad** al crear ejemplos, evitando incluir información sensible o que pueda comprometer la seguridad de la plataforma.
*   Mantener la coherencia con los dominios principales (`alphapp.xyz`) facilita la **organización del código** y la **documentación**.
*   La API se documenta en `docs/api/`. La documentación del proyecto en general se encuentra en el directorio `docs/`.
