# Clase 2: Requerimientos de Software — Nivel 2

Esta clase profundiza en la transición de las necesidades informales de los usuarios hacia especificaciones técnicas verificables.

---

## Definición Formal

Un requerimiento es una propiedad documentada y verificable que un sistema debe poseer para resolver un problema o alcanzar un objetivo.

---

## Cualidades de un Requerimiento

Para que un requerimiento sea considerado profesional, debe cumplir las siguientes características:

- Necesario
- No ambiguo
- Verificable
- Consistente
- Completo
- Atómico
- Trazable

---

## Requerimientos Funcionales (RF)

Los Requerimientos Funcionales describen **qué hace el sistema** mediante acciones concretas, tareas o cálculos.

### Plantilla de Redacción

```text
El sistema deberá [acción] [objeto] [condición].
```

### Ejemplo

```text
El sistema deberá permitir consultar apuntes organizados por materia.
```

---

## Requerimientos No Funcionales (RNF)

Los Requerimientos No Funcionales describen **cómo debe comportarse el sistema**.

Incluyen aspectos relacionados con:

- Rendimiento
- Seguridad
- Usabilidad
- Escalabilidad
- Disponibilidad

> Un RNF sin métrica es solo un deseo.

Por ello, todo requerimiento no funcional debe:

- Ser medible.
- Tener un umbral aceptable.
- Poder verificarse.

### Ejemplo

```text
La plataforma deberá cargar en menos de 3 segundos.
```

---

## Atributos de Calidad (ISO/IEC 25010)

La norma ISO/IEC 25010 define ocho atributos principales de calidad del software:

| Atributo | Descripción |
|-----------|------------|
| Adecuación funcional | Cumplimiento de funciones requeridas |
| Eficiencia | Uso óptimo de recursos |
| Compatibilidad | Integración con otros sistemas |
| Usabilidad | Facilidad de uso |
| Confiabilidad | Funcionamiento estable |
| Seguridad | Protección de la información |
| Mantenibilidad | Facilidad de modificación |
| Portabilidad | Adaptación a diferentes plataformas |

---

## Historias de Usuario

Las Historias de Usuario permiten capturar necesidades desde la perspectiva del usuario.

### Estructura

```text
Como [usuario],
quiero [acción],
para [beneficio].
```

### Ejemplo

```text
Como estudiante,
quiero acceder a los apuntes de clase,
para ponerme al día cuando falte al colegio.
```

---

## Criterio INVEST

Toda historia de usuario debe cumplir con el modelo INVEST:

| Letra | Significado |
|--------|-------------|
| I | Independiente |
| N | Negociable |
| V | Valiosa |
| E | Estimable |
| S | Small (Pequeña) |
| T | Testable (Comprobable) |

---

# Resumen General

- Los requerimientos convierten necesidades en especificaciones técnicas.
- Los RF describen lo que hace el sistema.
- Los RNF describen cómo debe comportarse.
- Los atributos de calidad garantizan software robusto y usable.
- Las historias de usuario facilitan la comprensión de necesidades reales.
- INVEST ayuda a crear historias claras y funcionales.