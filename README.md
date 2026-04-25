# SheVan — Web

Sitio web multipágina para [SheVan](https://shevanbarcelona.es), camperizadora artesanal en Sabadell, Barcelona.

Sitio estático generado desde Python — **25 páginas indexables**, optimizado para SEO local (Sabadell, Barcelona, Catalunya), responsive y desplegable en cualquier hosting (Netlify, Vercel, GitHub Pages, IONOS, lo que sea).

---

## 🚀 Quick start

Necesitas Python 3.8 o superior. **Sin dependencias externas** — solo stdlib.

```bash
git clone <este-repo>
cd shevan-web

# Generar el sitio
python build.py

# Generar con CSS y logos inlineados (cada página = archivo autónomo)
python build.py --inline
```

El sitio se genera en `dist/`. Ábrelo en navegador con `open dist/index.html` (o doble click en el archivo).

---

## 📁 Estructura del repo

```
shevan-web/
├── build.py                    # Punto de entrada CLI
├── src/                        # Generador (Python)
│   ├── shared.py               # CSS y datos de contacto (config global)
│   ├── data.py                 # Contenido editable de cada servicio
│   ├── templates.py            # Renderizadores: head, nav, footer…
│   ├── builder.py              # Lógica de páginas y build_all()
│   └── inliner.py              # Inliner opcional de assets
├── assets/                     # Logos fuente (PNG)
│   ├── logo-yellow.png
│   └── logo-black.png
├── dist/                       # Sitio generado (git-ignorable)
│   ├── index.html
│   ├── styles.css
│   ├── camperizaciones.html  +  camperizaciones/{...}.html
│   ├── accesorios.html       +  accesorios/{...}.html
│   ├── taller.html           +  taller/{...}.html
│   ├── proyectos.html
│   └── contacto.html
├── README.md
└── DEPLOY.md                   # Guía de despliegue paso a paso
```

---

## ✏️ Cómo editar el contenido

**El contenido vive en `src/data.py`** — diccionarios de Python con título, descripción, meta SEO, etc. de cada servicio.

Por ejemplo, para cambiar el texto del servicio "Techo Elevable":

```python
# src/data.py
{
    "slug": "techo-elevable",
    "title": "Techo Elevable",
    "lead": "¿Sientes que a tu aventura le falta espacio?",
    "intro": "El techo elevable es la transformación definitiva...",
    # ...edita aquí
}
```

Después regenera el sitio con `python build.py`.

**Datos de contacto** (teléfono, email, dirección, horario): `src/shared.py` → `CONTACT`.

**Estilos CSS**: `src/shared.py` → variable `CSS`. Cambia los tokens al principio (`--yellow`, `--ink`, etc.) si quieres tocar el color base.

---

## 🌐 Despliegue

Mira [DEPLOY.md](./DEPLOY.md) para la guía completa. Resumen rápido:

- **Netlify / Vercel**: arrastra `dist/` a la web del servicio → URL inmediata gratis.
- **GitHub Pages**: en settings del repo, source = `dist/` → publicado automáticamente.
- **Hosting tradicional (IONOS, Hostinger…)**: subir `dist/` por FTP a `public_html/`.

---

## 🔍 SEO

Cada página tiene:
- `<title>` y `<meta description>` únicos optimizados por keyword
- Schema.org `LocalBusiness` / `AutoRepair` / `Service` (JSON-LD)
- Open Graph + Twitter Card
- Geo tags (Sabadell, Catalunya, lat/lng)
- Canonical URL
- Breadcrumbs HTML semánticos

URLs limpias y jerárquicas para indexación independiente:

| URL | Keyword principal |
|-----|------------------|
| `/camperizaciones/gran-volumen.html` | camperizar Ducato Sabadell |
| `/camperizaciones/medianas-pequenas.html` | camperizar VW T6 Barcelona |
| `/accesorios/techo-elevable.html` | instalar techo elevable Reimo |
| `/accesorios/calefaccion.html` | calefacción Webasto camper |
| `/taller/filtraciones.html` | reparar filtración camper |

**Pendiente para que el SEO trabaje al 100%** (no es código, es configuración):
- [ ] Google Business Profile (esto es el 50% del SEO local)
- [ ] Google Search Console + sitemap.xml + robots.txt
- [ ] Reseñas en Google de clientes
- [ ] Sustituir las imágenes placeholder por fotos reales con `alt` descriptivo

---

## 📬 Formulario de contacto

El formulario en `/contacto.html` usa **FormSubmit** (servicio gratuito, sin registro).

**Activación inicial — solo la primera vez:**
1. Despliega el sitio
2. Manda un envío de prueba
3. Llega un email a `info@shevanbarcelona.es` pidiendo confirmación
4. Click en confirmación → a partir de ese momento, todos los envíos llegan automáticamente

Si quieres cambiar de servicio (Formspree, Mailgun, Netlify Forms, etc.), edita el `action="..."` del `<form>` en `src/builder.py` → `render_contact_page()`.

---

## 🛠️ Stack técnico

- **Lenguaje**: Python 3.8+ (solo stdlib)
- **Output**: HTML5 estático + CSS3 + JS mínimo
- **Tipografías**: Bricolage Grotesque + Inter (Google Fonts, `display=swap`)
- **Sin dependencias** de Node, npm, frameworks, build tools
- **Sin tracking** por defecto (añadir Plausible/Analytics manualmente si se quiere)

---

## 📄 Licencia

Código y diseño propiedad de SheVan. Uso interno.
