# Sistema de Gestión de Hotel — Patagonia Hotel

Trabajo Práctico de Python — UTN FRRe

---

## Integrantes del grupo

| Nombre y Apellido | DNI |
|---|---|
| Juan Lucas Lautaro Gomez Contreras | [46718130] |
| [Ivo Milan Bruic] | [46963651] |
| [Enzo Ian Sanchez Borelli] | [47526155] |


---

## Descripción del sistema

Sistema de gestión hotelera desarrollado en Python que se ejecuta completamente por consola.  
Permite administrar huéspedes, habitaciones y reservas de un hotel, cubriendo el ciclo completo de check-in y check-out.

---

## Funcionalidades

- **Gestión de huéspedes**: registro, búsqueda por DNI y listado general.
- **Gestión de habitaciones**: visualización de todas las habitaciones, filtro por disponibilidad y por tipo (simple, doble, suite).
- **Check-in**: registro de ingreso de un huésped a una habitación con validación de fechas y cálculo automático del costo.
- **Check-out**: liberación de la habitación y resumen de la estadía.
- **Reservas activas**: listado de todas las reservas en curso.
- **Historial**: registro completo de todas las reservas (activas y finalizadas).
- **Estadísticas**:
  - Porcentaje de ocupación por tipo de habitación.
  - Ingresos totales y desglose por tipo de habitación.

---

## Estructura del proyecto

```
hotel_project/
│
├── main.py           # Punto de entrada. Menú principal y flujo de navegación.
├── habitaciones.py   # Módulo de habitaciones: datos, estados y estadísticas.
├── huespedes.py      # Módulo de huéspedes: registro y búsqueda.
├── reservas.py       # Módulo de reservas: check-in, check-out e historial.
├── validaciones.py   # Funciones de validación y entrada de datos por consola.
└── README.md         # Este archivo.
```

---

## Conceptos aplicados

| Concepto | Dónde se aplica |
|---|---|
| Estructuras condicionales | Validaciones en check-in, búsquedas, confirmaciones |
| Estructuras repetitivas | Menús con `while`, recorrido de listas con `for` |
| Funciones | Todos los módulos están modularizados en funciones |
| Validaciones | `validaciones.py` centraliza todas las entradas del usuario |
| Acumuladores y contadores | Cálculo de noches, ingresos totales, conteo de reservas |
| Modularización | Separación en 4 módulos temáticos + main |
| Manejo de errores | Mensajes claros al usuario ante entradas inválidas |

---

## Cómo ejecutar el sistema

### Requisitos
- Python 3.8 o superior instalado.
- No requiere instalar ninguna librería adicional.

### Pasos

1. Clonar el repositorio:
   
   git clone https://github.com/4ntis0c1al/hotel-los-andes
   cd hotel-los-andes
  

2. Ejecutar el programa:
   
   python main.py
   

---

## Flujo de uso típico

```
1. Registrar un huésped (Menú → Gestión de Huéspedes → 1)
2. Ver habitaciones disponibles (Menú → Gestión de Habitaciones → 2)
3. Realizar check-in (Menú → Check-in)
4. Consultar reservas activas (Menú → Reservas activas)
5. Realizar check-out cuando corresponda (Menú → Check-out)
6. Consultar estadísticas (Menú → Estadísticas)
```

---

## Decisiones de diseño

- **Sin bases de datos ni archivos externos**: todos los datos se almacenan en listas de diccionarios en memoria durante la ejecución, acorde al nivel de la materia.
- **Sin programación orientada a objetos**: se utilizan únicamente funciones, listas y diccionarios.
- **Módulo de validaciones centralizado**: todas las funciones de entrada del usuario están en `validaciones.py` para reutilización y claridad.
- **Cálculo de noches simplificado**: se utiliza una conversión a días basada en día + mes×30 + año×365, suficiente para los propósitos del trabajo.

---

