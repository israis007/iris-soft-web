# POS Estudio: checklist antes de beta

Este documento separa lo que ya está representado en la landing de lo que todavía debe validarse en la app móvil. No sustituye las pruebas reales en Samsung/tableta, Android, iOS y las tiendas.

## Ya comunicado en la landing

- Colecciones, carpetas y entornos.
- Scripts controlados y variables reutilizables.
- Respuestas legibles, exportación y trabajo local-first.
- REST, GraphQL, SOAP y WebSocket como objetivos del producto.
- Android e iOS como plataformas.

## Pendiente de validar en la app

### Importación y datos

- [ ] Importar colecciones Postman JSON desde archivos de hasta 50 MB.
- [ ] Decodificar y persistir en un hilo de I/O; nunca bloquear la UI.
- [ ] Mostrar progreso de lectura e inserción, deshabilitar Importar durante el parseo y mostrar estado circular al terminar.
- [ ] Confirmar reemplazo cuando la colección o carpeta ya exista.
- [ ] Conservar la jerarquía de carpetas y requests sin convertirla en una lista plana.

### Requests y protocolos

- [ ] Probar GET/POST/PUT/PATCH/DELETE, parámetros, headers y cuerpos.
- [ ] Completar body `none`, form-data, x-www-form-urlencoded, raw (JSON/JavaScript/XML/HTML), binary y GraphQL.
- [ ] Validar autenticación: No Auth, herencia, Basic, Bearer, JWT, Digest, OAuth 1/2, API Key, AWS Signature y NTLM cuando el cliente lo permita.
- [ ] Verificar SOAP/XML y WebSocket con una colección de ejemplo.
- [ ] Revisar redirects, HTTP version, TLS, certificados, pinning y proxy según las capacidades nativas.

### Scripts y variables

- [ ] Ejecutar pre-request y post-response en un sandbox limitado a la app.
- [ ] Validar `studio.environment`, variables globales/de colección y selección de entorno principal.
- [ ] Mapear respuestas como JSON, XML, YAML y HTML para guardar valores en variables.
- [ ] Ejecutar `studio.uuid.generate()` para idempotencia.
- [ ] Pedir GPS sólo cuando un script lo solicite explícitamente; no mantener ubicación en segundo plano.
- [ ] Mostrar consola de ejecución con errores, logs y duración.

### Response viewer

- [ ] Pestañas Body, Cookies, Headers (con total), Test Results y Export/Save.
- [ ] Intérpretes JSON, XML, YAML, HTML, JavaScript, Markdown, Raw, Hex y Base64.
- [ ] Preview con Beauty, búsqueda, vista de árbol y scroll horizontal para Hex.
- [ ] Detectar Base64 multimedia y ofrecer vista/descarga decodificada.
- [ ] Exportar el formato seleccionado y guardar la respuesta para diagnóstico offline.
- [ ] Mostrar código/etiqueta HTTP, tiempo, tamaño, IP local/remota, HTTP/TLS y certificado cuando estén disponibles.

### Rendimiento y persistencia

- [ ] Medir imports y respuestas grandes para evitar ANR/jank.
- [ ] Confirmar persistencia automática en Drift y recuperación después de cerrar la app.
- [ ] Probar offline-first, reintentos, cancelación y límites de memoria.

### Servicios y publicación

- [ ] Firebase/App Check: debug en desarrollo, proveedor de producción antes de liberar.
- [ ] Revisar permisos de notificaciones, biometría, cámara, archivos, ubicación y red por plataforma.
- [ ] Configurar RevenueCat (no “ReviewCat”) con productos, entitlement, restauración y enlaces de privacidad/términos.
- [ ] Preparar ficha de Google Play, Data Safety, contenido, testers y AAB firmado; dejar App Store para la siguiente ventana de revisión.
- [ ] Probar Android 10–17 en teléfono y tableta, y iOS 17+ antes de cerrar beta.

## Salida para pruebas beta

La app debe llegar a beta con una colección demo aislada (por ejemplo, PokeAPI), una base local limpia, un entorno de prueba y un reporte de fallos reproducible. Las pruebas reales quedan al final del plan, después de cerrar los puntos funcionales anteriores.

