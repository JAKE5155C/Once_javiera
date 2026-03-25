# Informe del Proyecto – Index.html (Soporte RIOT VALORANT)
### Inicio del trabajo

Se desarrolló un formulario web tipo “soporte al jugador”, enfocado en la gestión de consultas relacionadas con cuentas y servicios de Valorant.

El objetivo principal fue simular un sistema de tickets de ayuda, incorporando:

- Validación de campos obligatorios
- Selección de método de contacto preferido
- Estructura clara y fácil de usar para el usuario

Este enfoque permite recrear una experiencia similar a los sistemas reales de atención al cliente.

# Proyecto – styles.css (Diseño del soporte)
### Estructura general del diseño
Se definió una paleta de colores en `:root`, incluyendo colores primarios, secundarios, acentos, texto y fondos.
Se aplicó un reset global (`*`, `html`, `body`) para normalizar márgenes, box-sizing y tipografía.
### Contenedor principal
- `.contenedor`: establece un ancho máximo, centrado en pantalla, con padding y sombra suave para mejorar la presentación visual.
### Encabezado
- `.encabezado h1` y `p`: tipografía destacada, color blanco y uso de fondo oscuro o degradado para dar contraste.
### Formulario
- `.formulario-contacto`: diseño tipo tarjeta (card) con bordes redondeados, uso de grid y separación entre elementos (gap).
### Campos del formulario
- `.campo`: organización en columna (`flex-direction: column`) con espaciado uniforme.
- `.fila-doble`: estructura en dos columnas para pantallas grandes (`grid-template-columns: 1fr 1fr`) y adaptación a una sola columna en dispositivos móviles mediante media queries.
### Inputs y áreas de texto
- Estilos generales: padding, bordes redondeados y transiciones suaves.
- Estado `:focus`: resaltado visual con color azul para mejorar la interacción del usuario.
### Elementos adicionales
- `.obligatorio`: indica campos requeridos en color rojo.
- `.ayuda`: texto pequeño de apoyo o instrucciones.
- `.opciones-radio`: organización horizontal con buena separación y cursor interactivo.
- `#campo-telefono`: oculto por defecto, visible solo cuando es necesario.
Botones de acción
- `.acciones`: separación entre botones.
- `.btn-primario`: color llamativo para acciones principales.
- `.btn-secundario`: estilo neutro.
- Efecto hover: oscurecimiento para dar retroalimentación visual.
### Diseño responsive
`@media (max-width: 720px)`:
- Ajuste a una sola columna
- Botones de ancho completo
- Texto centrado
### Accesibilidad
- Uso de `:focus-visible`
- Buen contraste de colores
- Transiciones suaves para mejorar la experiencia del usuario

# Campo “Edad” (Index.html + styles.css)
### Estructura en HTML
- Se utiliza un `div.campo` para agrupar el elemento.
- `label for="edad"`: funciona como título descriptivo (“Edad *”).
- `input type="number"` con atributos:
  - `id="edad"` y `name="edad"`
  - `placeholder`: guía al usuario
  - `required`: campo obligatorio
  - `min="15"` y `max="99"`: validación de rango
### Estilos en CSS
- Inputs con ancho completo (`width: 100%`), padding y bordes redondeados.
- Estado `:focus`: resalta el campo activo.
- `span.ayuda`: proporciona contexto adicional si es necesario.
### Concepto visual

El diseño genera un “recuadro funcional” donde el usuario identifica fácilmente:
- El título del campo
- El espacio de entrada
- La validación implícita
### Mejoras opcionales
- Personalización del campo `#edad` con fondo suave
- Modificación de controles numéricos (`::-webkit-inner-spin-button`) para una apariencia más limpia.
