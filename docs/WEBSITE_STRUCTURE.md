# IRIsoft web: estructura y publicación

## Objetivo

IRIsoft funciona como un único portal y un único hosting. La portada presenta la marca y enlaza a cada producto; cada producto vive en su propia subcarpeta para poder evolucionar sin mezclar su código.

```text
iris-soft-web/
├── index.html                 # Página principal de IRIsoft
├── marketing.html             # Creative Studio / servicios
├── proyectos.html             # Portafolio de productos y colaboraciones
├── easy-pos-lan/              # Landing de Easy POS LAN
│   ├── index.html
│   └── legal/
├── pos-estudio/               # Landing de POS Estudio
│   └── index.html
├── resources/                 # Logos, imágenes y videos de IRIsoft
└── .htaccess                  # Directorio raíz, alias y redirects
```

## URLs públicas

- `https://irisoft.com.mx/` — portada IRIsoft.
- `https://irisoft.com.mx/easy-pos-lan/` — producto Easy POS LAN.
- `https://irisoft.com.mx/pos-estudio/` — producto POS Estudio.
- `https://irisoft.com.mx/marketing.html` — servicios de diseño, web y marketing.
- `https://irisoft.com.mx/proyectos.html` — productos propios y colaboraciones.

Los alias `/easypos` y `/api-studio` redirigen a las rutas canónicas. Las páginas de producto ya incluyen navegación de regreso a IRIsoft y enlaces cruzados.

## Fuente de cada landing

- Easy POS LAN se mantiene desde `antigravity/web` y se replica en `easy-pos-lan/` para publicación conjunta.
- POS Estudio se mantiene desde `api-studio-flutter/landing/public` y se replica en `pos-estudio/`.

Antes de publicar una nueva versión, hay que sincronizar la landing que haya cambiado, revisar enlaces y ejecutar la validación local. La copia dentro de este repositorio es deliberada: permite ajustar cada página como subproyecto sin romper la portada.

## Publicación pendiente

El dominio `irisoft.com.mx` ya resuelve y Apache responde, pero al momento de documentar esta estructura el document root todavía responde con un listado vacío. Además, la conexión TLS presenta un certificado que no coincide con el hostname, por lo que los clientes estrictos rechazan HTTPS. Para activar el portal:

1. Subir el contenido de `iris-soft-web/` (incluido `.htaccess`) al document root del hosting.
2. Confirmar que `index.html` sea el `DirectoryIndex`.
3. Instalar/renovar un certificado que cubra `irisoft.com.mx` y `www.irisoft.com.mx`, y forzar HTTPS con redirección de `www` a la URL canónica.
4. Verificar las cuatro URLs anteriores y las páginas legales.
5. Comprobar que las etiquetas canonical/Open Graph ya apunten a `irisoft.com.mx`.

No se considera desplegado hasta que esas URLs devuelvan las páginas nuevas desde el dominio.

La landing de POS Estudio sí está publicada y verificada en Firebase como
`https://pos-estudio.web.app`. Esta URL es temporal hasta decidir si el dominio
principal se migra a Firebase Hosting o si se sube el portal completo al
hosting Apache actual.
