# Clase 5: Introducción al Diseño

La introducción al diseño parte de una idea fundamental:

Diseñar no significa únicamente crear pantallas atractivas, sino tomar decisiones estratégicas sobre cómo funcionará el sistema y cómo interactuarán los usuarios con él.

En el proyecto Atlas, el diseño busca garantizar que los estudiantes puedan acceder fácilmente a apuntes, materiales y contenidos académicos desde cualquier dispositivo.

---

# Objetivo del Diseño

El diseño tiene como propósito:

- Mejorar la experiencia del usuario.
- Organizar la información de forma clara.
- Facilitar la navegación.
- Resolver problemas antes de programar.

Un buen diseño evita:

- Interfaces confusas.
- Funcionalidades innecesarias.
- Mala organización de contenidos.
- Problemas de usabilidad.

---

# Niveles de Diseño

El diseño de software evoluciona progresivamente desde ideas simples hasta prototipos interactivos.

---

## 1. Sketch (Boceto)

Es la representación más básica y rápida de una idea.

Se realiza generalmente a mano o mediante dibujos simples.

### Objetivo

- Explorar ideas rápidamente.
- Visualizar distribución inicial.
- Proponer soluciones sin invertir mucho tiempo.

### Características

- No contiene colores detallados.
- No requiere precisión.
- Se enfoca en estructura general.

### Ejemplo en Atlas

Un boceto de:

- Pantalla principal.
- Menú de materias.
- Zona de apuntes académicos.

---

## 2. Wireframe

El wireframe representa la estructura visual del sistema mediante cajas y elementos simples.

> Es el “esqueleto” de la interfaz.

### Objetivo

Definir:

- Ubicación de botones.
- Distribución de contenidos.
- Navegación principal.
- Jerarquía visual.

### Características

- Diseño simple.
- Sin colores finales.
- Centrado en funcionalidad y organización.

### Ejemplo en Atlas

Un wireframe podría incluir:

- Barra de navegación.
- Lista de materias.
- Área de visualización de documentos.
- Botón para compartir apuntes.

---

## 3. Mockup

El mockup agrega apariencia visual realista al diseño.

Incluye:

- Colores.
- Tipografía.
- Iconos.
- Estilo visual final.

### Objetivo

Mostrar cómo se verá realmente la plataforma.

### Características

- Diseño detallado.
- Aspecto profesional.
- No necesariamente interactivo.

### Ejemplo en Atlas

- Diseño visual moderno.
- Colores institucionales.
- Interfaz adaptable a dispositivos móviles.

---

## 4. Prototipo

El prototipo es una versión interactiva del diseño.

Permite simular:

- Navegación.
- Botones.
- Flujo de pantallas.
- Interacciones del usuario.

### Objetivo

Validar la experiencia antes de programar.

### Herramientas comunes

- Figma
- Adobe XD
- Sketch

### Ejemplo en Atlas

El estudiante podría:

1. Entrar a la plataforma.
2. Seleccionar una materia.
3. Consultar apuntes.
4. Descargar materiales.

Todo esto sin que el sistema esté programado todavía.

---

# Arquitectura de Software

La arquitectura de software define cómo se organizan las partes principales del sistema y cómo se conectan entre sí.

> Es el plano estructural del software.

---

## Componentes Principales

En Atlas, la arquitectura puede incluir:

### Frontend

Parte visible para el usuario.

Incluye:

- Interfaz web.
- Navegación.
- Formularios.
- Visualización de contenidos.

### Backend

Gestiona la lógica interna del sistema.

Incluye:

- Usuarios.
- Autenticación.
- Gestión de archivos.
- Procesamiento de información.

### Base de Datos

Almacena:

- Apuntes.
- Materias.
- Usuarios.
- Materiales académicos.

### APIs

Permiten la comunicación entre frontend y backend.

---

# Diagramas Utilizados

La arquitectura se representa mediante diagramas que ayudan a comprender el funcionamiento del sistema.

---

## Diagramas de Flujo

Representan procesos paso a paso.

### Ejemplo

```text
Inicio sesión → Selección de materia → Consulta de apuntes → Descarga de archivo
```

---

## Diagramas de Secuencia

Muestran cómo interactúan los componentes del sistema en el tiempo.

### Ejemplo en Atlas

1. El usuario solicita un documento.
2. El frontend envía la solicitud al backend.
3. El backend consulta la base de datos.
4. El sistema devuelve el archivo solicitado.

---

# Importancia del Diseño

Un buen diseño permite:

- Detectar errores antes de programar.
- Ahorrar tiempo y recursos.
- Mejorar la experiencia del usuario.
- Facilitar el mantenimiento del sistema.

Un mal diseño puede provocar:

- Interfaces confusas.
- Usuarios frustrados.
- Mala organización.
- Problemas técnicos futuros.

---

# Buenas Prácticas de Diseño

- Diseñar pensando en el usuario.
- Mantener interfaces simples.
- Evitar sobrecargar las pantallas.
- Priorizar accesibilidad y claridad.
- Validar diseños antes de programar.
- Adaptar la interfaz a diferentes dispositivos.

---

# Resumen General

- Diseñar implica tomar decisiones estratégicas antes de programar.
- El proceso evoluciona desde sketches hasta prototipos interactivos.
- Los wireframes ayudan a organizar la estructura visual.
- Los mockups muestran la apariencia final del sistema.
- Los prototipos permiten validar la experiencia del usuario.
- La arquitectura de software organiza los componentes principales del sistema.
- Los diagramas ayudan a comprender el funcionamiento interno de la plataforma.
- Un buen diseño mejora la calidad y usabilidad del software.