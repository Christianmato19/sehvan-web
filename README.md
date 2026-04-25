[README.md](https://github.com/user-attachments/files/27088720/README.md)
# SheVan — Web multipágina

Sitio estático de 25 páginas para SheVan, listo para subir a cualquier hosting (Netlify, Vercel, Hostinger, IONOS, lo que sea).

---

## 1. Estructura

```
shevan_web/
├── index.html                           # Home
├── styles.css                           # Estilos compartidos
├── logo-yellow.png                      # Logo amarillo (sobre fondos oscuros)
├── logo-black.png                       # Logo negro (sobre fondos claros)
│
├── camperizaciones.html                 # Overview de camperizaciones
├── camperizaciones/
│   ├── gran-volumen.html
│   ├── medianas-pequenas.html
│   └── homologaciones.html
│
├── accesorios.html                      # Overview de accesorios
├── accesorios/
│   ├── segunda-bateria.html
│   ├── paneles-solares.html
│   ├── inversor.html
│   ├── calefaccion.html
│   ├── aire-acondicionado.html
│   ├── aislamiento.html
│   ├── ventanas-claraboyas.html
│   ├── techo-elevable.html
│   ├── cierres-seguridad.html
│   ├── toldo-portabicis.html
│   └── suspension-neumatica.html
│
├── taller.html                          # Overview de taller / reparaciones
├── taller/
│   ├── electrica.html
│   ├── agua.html
│   ├── filtraciones.html
│   ├── gas.html
│   └── mobiliario.html
│
├── proyectos.html
└── contacto.html
```

**Total: 25 páginas HTML + CSS + 2 logos**

Cada URL es indexable por Google de forma independiente. Cada una tiene su propio `<title>`, `<meta description>`, schema.org marcado y canonical.

---

## 2. Subir a hosting

Es HTML estático puro. **No necesita PHP, base de datos ni servidor**. Sube todo el contenido de la carpeta `shevan_web/` al directorio raíz del hosting.

**Opciones recomendadas:**
- **Netlify** (gratis): arrastra la carpeta a netlify.com → URL inmediata. Ideal para pruebas.
- **Vercel** (gratis): igual de fácil que Netlify.
- **Hosting tradicional** (IONOS, Hostinger, etc.): subir vía FTP a `public_html/`.

Para que las URLs salgan limpias (`/accesorios/techo-elevable/` en vez de `/accesorios/techo-elevable.html`), Netlify y Vercel lo hacen automático. En hosting tradicional habría que configurar `.htaccess`.

---

## 3. Formulario de contacto (IMPORTANTE)

El formulario en `contacto.html` envía los datos al email de Silvia mediante **FormSubmit** (servicio gratuito, sin registro).

### Activación inicial (solo la primera vez):

1. Sube el sitio al hosting
2. Entra en `/contacto.html` y manda **un envío de prueba** rellenando el formulario
3. Llegará un email a `info@shevanbarcelona.es` pidiendo confirmar la activación. **Click en ese email**
4. A partir de ese momento, todos los envíos del formulario llegan al correo de Silvia automáticamente

**Si quieres cambiar de servicio** (ej: usar Formspree, Mailgun, Netlify Forms…) basta con cambiar el `action="..."` del `<form>` en `contacto.html`.

---

## 4. Lo que falta por completar

### Imágenes
Cada página de servicio tiene un placeholder visual claramente marcado donde irá la foto real. Sustituir por:

- **Camperizaciones / Gran Volumen** → foto de Ducato/Sprinter terminada por dentro
- **Camperizaciones / Medianas y Pequeñas** → foto de T6/Vito terminada
- **Cada accesorio** → foto del trabajo terminado (segunda batería instalada, panel solar en techo, etc.)
- **Cada sección de taller** → foto del proceso o herramienta
- **Proyectos** → galería real de furgos terminadas

### Textos pendientes de revisión
Los textos vienen del documento de contenido del cliente. Las únicas adiciones inventadas son las descripciones de proyectos placeholder en `proyectos.html` (sustituir por casos reales).

### Logos de marcas (camperizaciones)
Las páginas Gran Volumen y Medianas/Pequeñas listan las marcas en chips de texto. Si Silvia quiere logos reales (Fiat, Peugeot, Mercedes...), reemplazar los `.brand-chip` por imágenes en `<img>`.

### Aviso legal / política de privacidad / cookies
Los enlaces del footer apuntan a `#`. Crear las páginas legales correspondientes (obligatorio en España por RGPD).

---

## 5. SEO — checklist para que indexe bien

### Lo que ya está hecho ✓
- [x] `<title>` único en cada página, optimizado por keywords ("Instalación de Techo Elevable Reimo en Sabadell")
- [x] `<meta description>` única por página
- [x] Schema.org `LocalBusiness` / `AutoRepair` en home
- [x] Schema.org `Service` en cada servicio
- [x] Open Graph + Twitter Card en todas
- [x] Canonical URLs
- [x] Geo tags (Sabadell, Catalunya)
- [x] HTML semántico (header, nav, main, article, footer)
- [x] Estructura de URLs limpia y jerárquica
- [x] Mobile responsive
- [x] Carga rápida (todo estático, fuentes con `display=swap`)

### Lo que tiene que hacer Marta (o quien gestione)
- [ ] **Google Business Profile** — fichar SheVan en Google Maps (es el 50% del SEO local)
- [ ] **Google Search Console** — añadir el dominio y enviar el sitemap
- [ ] **Sitemap.xml** — generar con [xml-sitemaps.com](https://www.xml-sitemaps.com) y subir a la raíz
- [ ] **robots.txt** — crear con `Sitemap: https://shevanbarcelona.es/sitemap.xml`
- [ ] **HTTPS** — el hosting tiene que servir con certificado SSL (Netlify/Vercel ya lo dan automático)
- [ ] **Reseñas en Google Business** — pedir review a cada cliente que entrega su furgo
- [ ] **Alt text en imágenes** — cuando se sustituyan los placeholders, escribir alt descriptivo ("Camperización VW T6 con cama elevable")
- [ ] Configurar **Google Analytics** o **Plausible** para medir visitas
- [ ] Configurar `_redirects` (Netlify) o `.htaccess` para que `/accesorios/techo-elevable/` redirija a `.html`

### Para SEO local (Sabadell, Barcelona, Vallès)
- Consistencia NAP (Name, Address, Phone): debe estar exactamente igual en web, Google Business, redes sociales y directorios
- Mencionar Sabadell, Polígono Can Roqueta, Vallès Occidental y Barcelona de forma natural en los textos
- Dar de alta en directorios locales: Páginas Amarillas, Yelp, etc.

---

## 6. Cómo regenerar el sitio si cambia el contenido

Las páginas se generan desde un script Python (`build/04_render_and_build.py`). El contenido vive en `build/02_data.py` como diccionarios. Para cambiar texto:

1. Edita el diccionario correspondiente en `02_data.py`
2. Ejecuta `python3 04_render_and_build.py`
3. Los HTML se regeneran con los nuevos textos

Esto es opcional — Marta también puede editar los HTML directamente si prefiere.

---

## 7. Performance esperada

- **PageSpeed**: 95+ móvil, 100 desktop (al sustituir las imágenes habrá que comprimirlas)
- **Lighthouse SEO**: 100
- **Lighthouse Accessibility**: 95+
- **Tamaño total inicial**: ~150KB (sin imágenes)

---

## Contacto técnico

Cualquier duda sobre cómo está montado o cómo modificarlo, escríbeme — en cualquier caso, todo es HTML/CSS estándar y cualquier diseñadora puede tocar lo que sea.
