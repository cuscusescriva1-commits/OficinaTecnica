# Oficina técnica

Tycoon idle/incremental para móvil en vista isométrica. Diriges una oficina de ingeniería: aceptas encargos de clientes, tus empleados dibujan los planos, cobras y la oficina crece de forma visible (cuadros en la pared, mesas, ordenadores, plóter, certificaciones…). Estética de papel de plano (azul `#123A5E`, amarillo señal `#F2B705`). Interfaz en español.

Todo el juego es un único `index.html` autocontenido (CSS y JS inline, sin librerías). Solo carga las tipografías Barlow desde Google Fonts, con `system-ui` como alternativa.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html` | El juego completo |
| `manifest.webmanifest` | Datos de la app instalable (PWA) |
| `sw.js` | Service worker: funciona sin conexión (red primero, caché de reserva) |
| `icon-180.png`, `icon-192.png`, `icon-512.png` | Iconos (`tools/icons.py` los genera con Python y PIL) |
| `.nojekyll` | Evita que GitHub Pages procese los archivos con Jekyll |

## Cómo publicarlo (GitHub Pages)

1. Sube el repositorio a GitHub (la carpeta `oficina-tecnica/` en la raíz).
2. En el repositorio: **Settings → Pages → Build and deployment → Deploy from a branch**.
3. Elige la rama `main` y la carpeta `/ (root)`, y pulsa **Save**.
4. Espera uno o dos minutos. El juego quedará en
   `https://TU_USUARIO.github.io/NOMBRE_DEL_REPO/oficina-tecnica/`.

Para probarlo en local: `cd oficina-tecnica && python3 -m http.server 8000` y abre `http://localhost:8000`.

## Añadirlo a la pantalla de inicio del iPhone

1. Abre la URL del juego en **Safari** (no en el navegador integrado de otra app).
2. Toca el botón **Compartir** (el cuadrado con la flecha hacia arriba).
3. Elige **Añadir a pantalla de inicio** y confirma con **Añadir**.
4. Ábrelo desde el icono: se ve a pantalla completa y funciona sin conexión.

## Pasar la partida a otro dispositivo

1. En el dispositivo de origen: botón **Sede → Partida → Copiar partida**. Se copia un código (base64 del JSON de la partida).
2. En el dispositivo de destino: **Sede → Partida**, pega el código en el cuadro de texto y pulsa **Cargar partida**.

La partida se guarda sola en el navegador (`localStorage`, clave `oficina-tecnica-v2`) cada 4 segundos, al ocultar la página y al cerrarla. Al volver se simulan hasta 8 horas sin conexión (si no quedan proyectos activos ni jefe de proyecto, la oficina «cierra»).

## Cómo se juega

- **Toca a un cliente** de recepción y acepta su encargo. Pasa a la mesa de proyectos.
- **Toca los planos** de la mesa para avanzar a mano (racha de toques = más avance). Tus empleados avanzan los proyectos en orden.
- Cobras el 50 % mientras se trabaja y el resto al entregar. Entregar da reputación, que desbloquea clientes mejores, personal y mejoras.
- Contrata personal, amplía la oficina, compra herramientas y certificaciones. Abre nuevas sedes para un bono permanente (+25 % de producción por sede).
- Toca los **regalos** que aparecen en el suelo y cobra los objetivos del banner inferior.
