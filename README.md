# Clasificador de Temperaturas

**Reto Semana 2 — Programación para Ciencia de Datos**
Instituto Politécnico Nacional | Semestre Febrero-Julio 2026

---

## Autor

| Campo        | Datos                                      |
|--------------|--------------------------------------------|
| **Nombre**   | Diego Jehu Bustamante Villanueva           |
| **Grupo**    | 3AM1                                       |
| **Materia**  | Programación para Ciencia de Datos         |
| **Profesor** | Mario Augusto                              |
| **Escuela**  | Instituto Politécnico Nacional             |

---

## Descripción

Programa en Python que lee un archivo CSV con temperaturas de ciudades del mundo (en Celsius o Fahrenheit), las convierte todas a Celsius y clasifica cada ciudad según su clima.

```
Entrada (CSV mixto)          Programa              Salida (CSV limpio)
─────────────────────        ────────────          ───────────────────────
CDMX,22,C                                          CDMX,22.0,Templado
Nueva York,50,F    ──────>   main.py   ──────>     Nueva York,10.0,Frio
Moscu,-10,C                                        Moscu,-10.0,Congelante
```

---

## Estructura del Proyecto

```
reto-semana-02/
├── README.md              ← Este archivo
├── main.py                ← Programa principal
├── entrada.txt            ← Archivo de prueba normal (6 ciudades)
├── entrada_50.txt         ← Archivo de prueba con 50 ciudades
└── entrada_prueba.txt     ← Archivo de prueba con casos límite y errores
```

---

## Cómo Ejecutar

### Requisitos
- Python 3.x instalado
- Linux / macOS / Windows

### Uso básico

```bash
python3 main.py < entrada.txt
```

Esto imprime el resultado en pantalla (stdout).

### Guardar la salida en un archivo

```bash
python3 main.py < entrada.txt > salida.txt
```

### Ver resultado en pantalla inmediatamente

```bash
python3 main.py < entrada.txt | cat
```

### Ejecutar y guardar al mismo tiempo

```bash
python3 main.py < entrada.txt > salida.txt && cat salida.txt
```

---

## Formato de Entrada

Archivo CSV con encabezado obligatorio:

```
ciudad,temperatura,unidad
```

| Columna       | Tipo   | Descripción              | Ejemplos           |
|---------------|--------|--------------------------|--------------------|
| `ciudad`      | texto  | Nombre de la ciudad      | CDMX, Tokyo, Miami |
| `temperatura` | número | Valor de temperatura     | 22, -5, 98.6       |
| `unidad`      | texto  | C (Celsius) o F (Fahr.)  | C, F, c, f         |

### Ejemplo de archivo de entrada

```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Miami,95,F
Cancun,30,C
Chicago,14,F
```

---

## Formato de Salida

CSV con encabezado:

```
ciudad,temperatura_celsius,clasificacion
```

| Columna                | Descripción                            |
|------------------------|----------------------------------------|
| `ciudad`               | Nombre original de la ciudad           |
| `temperatura_celsius`  | Temperatura convertida con 1 decimal   |
| `clasificacion`        | Categoría según la tabla de rangos     |

### Ejemplo de salida

```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
Miami,35.0,Calido
Cancun,30.0,Calido
Chicago,-10.0,Congelante
```

---

## Tabla de Clasificación

| Temperatura (°C)   | Clasificación |
|--------------------|---------------|
| Menor a 0          | Congelante    |
| De 0 a 15          | Frio          |
| De 16 a 25         | Templado      |
| De 26 a 35         | Calido        |
| Mayor a 35         | Extremo       |

---

## Fórmula de Conversión

Para convertir Fahrenheit → Celsius:

```
C = (F - 32) × 5 / 9
```

| Fahrenheit | Celsius | Clasificación |
|-----------|---------|---------------|
| 32°F      | 0.0°C   | Frio          |
| 50°F      | 10.0°C  | Frio          |
| 68°F      | 20.0°C  | Templado      |
| 95°F      | 35.0°C  | Calido        |
| 104°F     | 40.0°C  | Extremo       |

---

## Manejo de Errores

El programa **ignora silenciosamente** las líneas inválidas, sin mostrar mensajes de error:

| Tipo de error                        | Ejemplo                  |
|--------------------------------------|--------------------------|
| Temperatura no es número             | `Error,abc,C`            |
| Unidad inválida (no es C ni F)       | `Miami,95,X`             |
| Línea con menos o más de 3 columnas  | `Solo,doscolumnas`       |
| Línea vacía                          | *(línea en blanco)*      |

> **Nota:** Las unidades en minúsculas (`c`, `f`) sí son válidas y se procesan correctamente.

---

## Archivos de Prueba incluidos

### `entrada.txt` — Prueba básica
```bash
python3 main.py < entrada.txt > salida.txt
```
6 ciudades normales. Ideal para verificar que el programa funciona.

### `entrada_50.txt` — Prueba completa
```bash
python3 main.py < entrada_50.txt > salida_50.txt
```
50 ciudades de todo el mundo. Cubre todas las clasificaciones y conversiones F→C.

### `entrada_prueba.txt` — Casos límite y errores
```bash
python3 main.py < entrada_prueba.txt > salida_prueba.txt
```
Incluye temperaturas exactamente en los límites (0, 15, 16, 25, 26, 35, 36), valores inválidos, unidades incorrectas y líneas malformadas. Sirve para verificar robustez del programa.

---

## 💻 Código Fuente

```python
import sys

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9

def clasificar(celsius):
    """Clasifica la temperatura según rangos definidos."""
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"

def main():
    print("ciudad,temperatura_celsius,clasificacion")
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(',')
        if len(partes) != 3:
            continue

        ciudad   = partes[0].strip()
        temp_str = partes[1].strip()
        unidad   = partes[2].strip().upper()

        if unidad not in ['C', 'F']:
            continue

        try:
            temp = float(temp_str)
        except ValueError:
            continue

        celsius = fahrenheit_a_celsius(temp) if unidad == 'F' else temp
        clasificacion = clasificar(celsius)
        print(f"{ciudad},{celsius:.1f},{clasificacion}")

if __name__ == "__main__":
    main()
```

---

## Comandos Rápidos (Resumen)

```bash
# Ejecutar con entrada básica
python3 main.py < entrada.txt

# Guardar salida en archivo
python3 main.py < entrada.txt > salida.txt

# Prueba con 50 registros
python3 main.py < entrada_50.txt > salida_50.txt

# Prueba con casos límite y errores
python3 main.py < entrada_prueba.txt > salida_prueba.txt

# Ver el archivo de salida
cat salida.txt
```

---

*Reto Semana 2 — Programación para Ciencia de Datos — IPN 2026*