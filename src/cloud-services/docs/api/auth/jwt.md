# Autenticación con JWT en la API de Servicios en la Nube de Alphapp

Esta guía proporciona información detallada sobre cómo utilizar JSON Web Tokens (JWT) para la autenticación y autorización en la API de servicios en la nube de Alphapp.

## ¿Qué son los JWT?

JSON Web Tokens (JWT) son un estándar abierto (RFC 7519) para transmitir de forma segura información como un objeto JSON compacto. En el contexto de la API de Alphapp, los JWT se utilizan para verificar la identidad de los usuarios y autorizar el acceso a los recursos protegidos.

## Obtención de un Token JWT

Para obtener un token JWT, debes enviar una solicitud `POST` a la ruta `/auth/login` con tus credenciales (nombre de usuario y contraseña).

**Ejemplo de Solicitud:**

```json
{
  "username": "tuUsuario",
  "password": "tuContraseña"
}
```

**Ejemplo de Respuesta Exitosa (Código 200 OK):**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

**Campos del Token:**

*   `token`: El token JWT que se utilizará para autenticar las solicitudes.

## Uso del Token JWT

Una vez que obtengas un token JWT, debes incluirlo en el encabezado `Authorization` de todas las solicitudes posteriores a los recursos protegidos. El formato del encabezado debe ser `Bearer <token>`, donde `<token>` es el token JWT que obtuviste.

**Ejemplo de Solicitud:**

```
GET /users/123
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

## Verificación del Token JWT

El backend de la API verificará la validez del token JWT en cada solicitud. Si el token es inválido o ha expirado, la API devolverá un código de error 401 (No autorizado).

**Posibles Errores:**

*   `401 Unauthorized`: El token JWT es inválido, ha expirado o no se ha proporcionado.

## Renovación del Token JWT

Los tokens JWT tienen una fecha de expiración. Para obtener un nuevo token antes de que expire el actual, puedes utilizar un **token de refresco (refresh token)**. Envía una solicitud `POST` a la ruta `/auth/refresh` con tu token de refresco.

**Ejemplo de Solicitud:**

```json
{
  "refreshToken": "elTokenDeRefresco"
}
```

**Ejemplo de Respuesta Exitosa (Código 200 OK):**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NTY3ODkwMTIzIiwibmFtZSI6IkFuYWxpYSBGaW5layIsImlhdCI6MTUxNjIzOTAyMn0.yfHwT6ZtXvJp7W1uhCjYKi49J9JLxwNbcZKLg6EuQvo",
  "refreshToken": "elNuevoTokenDeRefresco"
}
```

**Campos de la Respuesta:**

*   `token`: El nuevo token JWT.
*   `refreshToken`: El nuevo token de refresco.

**Nota:** Guarda el nuevo token de refresco para futuras renovaciones.

## Estructura del Payload del JWT

El payload del JWT contiene información sobre el usuario autenticado. Aquí hay un ejemplo de la estructura del payload:

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "role": "admin",
  "iat": 1516239022,
  "exp": 1516242622
}
```

**Campos Comunes:**

*   `sub`: El identificador único del usuario.
*   `name`: El nombre del usuario.
*   `email`: La dirección de correo electrónico del usuario.
*   `role`: El rol del usuario (por ejemplo, "admin", "user").
*   `iat`: La marca de tiempo de emisión del token (en segundos desde la época Unix).
*   `exp`: La marca de tiempo de expiración del token (en segundos desde la época Unix).

## Seguridad de los JWT

Es importante tomar precauciones para proteger los tokens JWT:

*   **No almacenes los tokens JWT en el lado del cliente (por ejemplo, en localStorage o cookies) si no es necesario.** Considera usar cookies `HttpOnly` y `Secure` para mayor seguridad.
*   **Utiliza HTTPS para todas las comunicaciones con la API.**
*   **Mantén en secreto la clave secreta utilizada para firmar los tokens JWT.**
*   **Implementa una estrategia de rotación de claves para reducir el riesgo de que una clave comprometida se utilice para generar tokens JWT falsos.**

## Recursos Adicionales

*   **Documentación de la API:** [api.alphapp.xyz](https://api.alphapp.xyz)
*   **Ejemplos de Código:** [Enlace a ejemplos de código]
*   **Soporte:** [soporte@alphapp.xyz](mailto:soporte@alphapp.xyz)
*   **RFC 7519 (JSON Web Token):** [https://tools.ietf.org/html/rfc7519](https://tools.ietf.org/html/rfc7519)


### Explicación del código:

*   **Estructura del documento:**
    *   El documento está escrito en **Markdown**, lo que facilita su lectura y edición.
    *   Utiliza encabezados (`#`, `##`) para estructurar el contenido en secciones lógicas.
    *   Incluye **ejemplos de código en formato JSON** para mostrar la estructura de las solicitudes y respuestas de la API.
    *   Utiliza **bloques de código** (` ```json`) para resaltar los ejemplos de código.
    *   Incluye **notas y explicaciones adicionales** para aclarar conceptos y proporcionar información importante.
*   **Explicación detallada de JWT:**
    *   Describe **qué son los JWT** y cómo se utilizan en la API de Alphapp.
    *   Explica **cómo obtener, usar, verificar y renovar los tokens JWT**.
    *   Proporciona **ejemplos completos** de solicitudes y respuestas para cada paso.
    *   Describe la **estructura del payload del JWT** y los campos comunes.
*   **Consideraciones de seguridad:**
    *   Incluye **recomendaciones de seguridad** para proteger los tokens JWT.
*   **Recursos adicionales:**
    *   Proporciona **enlaces a la documentación completa de la API**, ejemplos de código, soporte y la especificación RFC 7519.

### Consideraciones adicionales:

*   Este es solo un ejemplo básico. Dependiendo de los requisitos de la API de Alphapp, el archivo podría incluir información adicional, como:
    *   **Algoritmos de firma soportados**.
    *   **Claims personalizados**.
    *   **Manejo de errores específicos de JWT**.
    *   **Integración con otros servicios de autenticación**.

*   Es importante que los ejemplos de código sean **válidos y representativos** de los datos que se envían y se reciben a través de la API.
*   Este archivo Markdown sirve como **documentación para los desarrolladores** que utilizarán la API, mostrándoles cómo implementar la autenticación y autorización con JWT.
*   Los ejemplos deben reflejar todos los campos definidos en el esquema y deben ser coherentes con los ejemplos de solicitudes y respuestas en formato JSON.
*   La correcta definición de la guía sobre JWT es fundamental para la **integración con la plataforma central** (`alphapp.xyz`) a través de la API. También promueve la **modularidad** dentro de la estructura de carpetas.
*   Este archivo de documentación ayuda a asegurar que la API se utilice correctamente y cumple con los requisitos de la plataforma Alphapp, facilitando el **desarrollo de aplicaciones y servicios**.
*   Es importante considerar las **pruebas de seguridad** al crear ejemplos, evitando incluir información sensible o que pueda comprometer la seguridad de la plataforma.
*   Mantener la coherencia con los dominios principales (`alphapp.xyz`) facilita la **organización del código** y la **documentación**.
*   La API se documenta en `docs/api/`. La documentación del proyecto en general se encuentra en el directorio `docs/`.

Este archivo proporciona una base sólida para la guía de autenticación con JWT en la API de servicios en la nube de Alphapp, facilitando su adopción y uso por parte de los desarrolladores.

