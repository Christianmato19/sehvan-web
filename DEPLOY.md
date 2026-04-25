# Guía de despliegue

El sitio se genera como HTML estático puro. **No necesita servidor PHP, base de datos, ni nada especial**. Lo único que tiene que servir el hosting son archivos `.html`, `.css` y `.png`.

---

## Opción 1 — Netlify (recomendada)

**La más fácil.** Gratis, HTTPS automático, dominio incluido (o conectas el tuyo).

1. Genera el sitio: `python build.py`
2. Ve a [netlify.com](https://netlify.com) y haz cuenta (gratis)
3. Pestaña "Sites" → arrastra la carpeta `dist/` al área de drop
4. Listo: te da una URL tipo `https://amazing-tesla-1234.netlify.app`
5. Para conectar el dominio `shevanbarcelona.es`:
   - Site settings → Domain management → Add custom domain
   - Cambiar los DNS según las instrucciones que te dé Netlify

**Para que `/camperizaciones/gran-volumen` funcione sin la extensión `.html`**, crea un archivo `dist/_redirects` con:
```
/*.html       /:splat       200
```

---

## Opción 2 — Vercel

Igual de fácil que Netlify.

1. `python build.py`
2. [vercel.com](https://vercel.com) → cuenta gratis
3. "New Project" → arrastra `dist/`
4. URL inmediata, HTTPS, todo gratis

---

## Opción 3 — GitHub Pages

Si ya tienes el repo en GitHub:

1. `python build.py` (genera `dist/`)
2. Commit y push de `dist/`
3. En GitHub: Settings → Pages → Source = `main` branch, folder = `/dist`
4. Pasados 2-3 minutos, el sitio está en `https://<usuario>.github.io/<repo>/`

Para dominio propio: añade un archivo `dist/CNAME` con el contenido `shevanbarcelona.es` y configura los DNS apuntando a GitHub Pages.

---

## Opción 4 — Hosting tradicional (IONOS, Hostinger, Banahosting…)

1. `python build.py`
2. Conecta por FTP / sFTP con las credenciales del hosting
3. Sube **el contenido de `dist/`** (no la carpeta entera, sino lo que hay dentro) a `public_html/` o `www/`
4. Verifica que el dominio apunte a esa carpeta

Para URLs sin `.html`, crea un `.htaccess` en `public_html/` con:
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+)$ $1.html [L]
```

---

## Después de desplegar — checklist

### Paso 1: activar el formulario
1. Entra en `/contacto.html`
2. Manda un envío de prueba con datos reales
3. Llega un email a `info@shevanbarcelona.es` de FormSubmit pidiendo activar
4. Click en el enlace de activación
5. A partir de ahora, los envíos del formulario llegan al email automáticamente

### Paso 2: SEO básico
1. **Google Search Console** ([search.google.com/search-console](https://search.google.com/search-console))
   - Añade el dominio
   - Verifica la propiedad
   - Envía el sitemap.xml *(generar con [xml-sitemaps.com](https://www.xml-sitemaps.com))*

2. **Google Business Profile** ([business.google.com](https://business.google.com))
   - Crear ficha para SheVan
   - Categoría: "Taller de reparaciones de vehículos" + "Camperizadora"
   - Subir fotos del taller, proyectos, equipo
   - Verificar la dirección física

3. **robots.txt** — crear `dist/robots.txt`:
   ```
   User-agent: *
   Allow: /

   Sitemap: https://shevanbarcelona.es/sitemap.xml
   ```

### Paso 3: contenido pendiente
Cada página de servicio tiene un placeholder visual donde irá la foto real. Sustituir:

- Cada accesorio → foto del trabajo terminado
- Cada sección de taller → foto del proceso o herramienta
- Proyectos → galería real de furgos terminadas

Para sustituir las imágenes, en `src/builder.py` → función `render_detail_page()` busca `<div class="detail-img-placeholder">` y reemplázalo por un `<img src="..." alt="...">` apuntando a las fotos reales.

### Paso 4: páginas legales
Los enlaces "Aviso legal", "Política de privacidad", "Cookies" en el footer apuntan a `#`. Hay que crear esas páginas (obligatorio en España por RGPD). Lo más rápido es generarlas con [un servicio gratuito](https://www.iubenda.com/) y enlazarlas.

---

## Performance esperada

Con el sitio desplegado y compresión activa del hosting:

- **PageSpeed mobile**: 95+
- **PageSpeed desktop**: 100
- **Lighthouse SEO**: 100
- **Tamaño total inicial (sin imágenes)**: ~150KB

Cuando se sustituyan las imágenes placeholder por fotos reales, optimizar siempre con [tinypng.com](https://tinypng.com) y formato WebP donde sea posible.

---

## Regenerar el sitio

Si actualizas contenido en `src/data.py` o tocas estilos en `src/shared.py`:

```bash
python build.py
```

Tarda menos de un segundo. Después haces commit del `dist/` actualizado y push.

Si vas a desplegar en Netlify/Vercel con integración de Git, ellos ejecutan el build automáticamente al hacer push — solo configura el comando `python build.py` y el directorio de salida `dist/`.
