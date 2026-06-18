# Clase 4: Documentación de Requerimientos

La documentación de requerimientos tiene como objetivo formalizar toda la información obtenida durante el análisis y la elicitación.

Estos documentos sirven como:

- Guía para el equipo de desarrollo.
- Referencia para diseñadores y analistas.
- Base para las pruebas del sistema.
- Contrato funcional entre clientes y desarrolladores.

---

## Estándar IEEE 830

El estándar IEEE 830 establece cómo debe redactarse una Especificación de Requerimientos de Software (SRS).

Su propósito es garantizar que los requerimientos sean:

- Claros
- Organizados
- Verificables
- Comprensibles

---

## Estructura Básica del SRS

### 1. Introducción

Incluye:

- Propósito del sistema.
- Alcance del proyecto.
- Definición de usuarios.
- Objetivos principales.

### Ejemplo

```text
El propósito de Atlas es facilitar el acceso a apuntes y materiales escolares mediante una plataforma web educativa.
```

---

### 2. Descripción General

Presenta una visión global del sistema:

- Funcionalidades principales.
- Restricciones.
- Características generales.
- Relación con otros sistemas.

### Ejemplo

- Plataforma web accesible desde diferentes dispositivos.
- Organización de materiales por grado y materia.
- Acceso rápido a contenidos académicos.

---

### 3. Requisitos Específicos

Contiene:

- Requerimientos funcionales.
- Requerimientos no funcionales.
- Restricciones técnicas.
- Reglas de negocio.

### Ejemplo de RF

```text
El sistema deberá permitir consultar apuntes organizados por materia.
```

### Ejemplo de RNF

```text
La plataforma deberá responder en menos de 3 segundos.
```

---

# Casos de Uso

Los casos de uso son descripciones narrativas que explican cómo interactúa el usuario con el sistema paso a paso.

Ayudan a comprender:

- Qué hace el usuario.
- Cómo responde el sistema.
- Qué errores pueden ocurrir.

---

## Elementos de un Caso de Uso

### Actor

Persona o entidad que interactúa con el sistema.

### Ejemplo

- Estudiante
- Docente
- Administrador

---

### Escenario

Describe la situación que activa el caso de uso.

### Ejemplo

> Un estudiante desea consultar apuntes de matemáticas.

---

### Flujo Principal

Secuencia normal de acciones.

### Ejemplo

1. El estudiante inicia sesión.
2. Selecciona una materia.
3. El sistema muestra los apuntes disponibles.
4. El estudiante consulta el contenido.

---

### Excepciones

Describen situaciones donde algo falla o no ocurre como se esperaba.

### Ejemplo

- El archivo no existe.
- El sistema pierde conexión.
- El usuario no tiene permisos suficientes.

> Ignorar excepciones hace que el análisis se vea incompleto y poco profesional.

---

# Revisión Cruzada

La revisión cruzada consiste en que otros analistas o miembros del equipo revisen el documento antes de aprobarlo.

El objetivo es detectar:

- Ambigüedades.
- Contradicciones.
- Información faltante.
- Errores de redacción.
- Requerimientos poco claros.

---

## Importancia de la Revisión Cruzada

Un documento mal redactado puede generar:

- Errores de desarrollo.
- Malentendidos.
- Retrasos.
- Funcionalidades incorrectas.

Por eso, la revisión cruzada mejora:

- La calidad del documento.
- La claridad de los requerimientos.
- La comunicación del equipo.

---

# Buenas Prácticas de Documentación

- Utilizar lenguaje claro y directo.
- Evitar términos ambiguos como:
  - “rápido”
  - “fácil”
  - “moderno”
- Mantener estructura organizada.
- Documentar excepciones.
- Hacer requerimientos medibles.
- Revisar constantemente el documento.

---
