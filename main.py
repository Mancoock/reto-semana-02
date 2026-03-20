import sys                          # Línea 1: Importa el módulo sys para leer desde stdin

def fahrenheit_a_celsius(f):        # Línea 3: Define función de conversión, recibe 'f' (Fahrenheit)
    return (f - 32) * 5 / 9         # Línea 4: Aplica la fórmula F→C y retorna el resultado

def clasificar(celsius):            # Línea 6: Define función de clasificación, recibe temperatura en Celsius
    if celsius < 0:                 # Línea 7: Si es menor a 0...
        return "Congelante"         # Línea 8: ...retorna "Congelante"
    elif celsius <= 15:             # Línea 9: Si está entre 0 y 15 (inclusive)...
        return "Frio"               # Línea 10: ...retorna "Frio"
    elif celsius <= 25:             # Línea 11: Si está entre 16 y 25 (inclusive)...
        return "Templado"           # Línea 12: ...retorna "Templado"
    elif celsius <= 35:             # Línea 13: Si está entre 26 y 35 (inclusive)...
        return "Calido"             # Línea 14: ...retorna "Calido"
    else:                           # Línea 15: Si es mayor a 35...
        return "Extremo"            # Línea 16: ...retorna "Extremo"

def main():                                               # Línea 18: Función principal del programa
    print("ciudad,temperatura_celsius,clasificacion")     # Línea 19: Imprime encabezado del CSV de salida
    primera_linea = True                                  # Línea 20: Bandera para saltar el encabezado de entrada

    for linea in sys.stdin:                               # Línea 22: Lee cada línea del archivo de entrada (stdin)
        linea = linea.strip()                             # Línea 23: Elimina espacios y saltos de línea al inicio/fin

        if primera_linea:                                 # Línea 25: Si es la primera línea (el encabezado)...
            primera_linea = False                         # Línea 26: ...marca que ya no es la primera
            continue                                      # Línea 27: ...y la salta (no la procesa)

        if not linea:                                     # Línea 29: Si la línea quedó vacía después del strip...
            continue                                      # Línea 30: ...la ignora

        partes = linea.split(',')                         # Línea 32: Separa la línea por comas → lista [ciudad, temp, unidad]
        if len(partes) != 3:                              # Línea 33: Si no tiene exactamente 3 columnas...
            continue                                      # Línea 34: ...la ignora

        ciudad   = partes[0].strip()                      # Línea 36: Extrae el nombre de la ciudad
        temp_str = partes[1].strip()                      # Línea 37: Extrae la temperatura como texto
        unidad   = partes[2].strip().upper()              # Línea 38: Extrae la unidad y la convierte a mayúsculas (c→C, f→F)

        if unidad not in ['C', 'F']:                      # Línea 40: Si la unidad no es C ni F...
            continue                                      # Línea 41: ...ignora la línea

        try:                                              # Línea 43: Intenta convertir la temperatura a número decimal
            temp = float(temp_str)                        # Línea 44: Convierte el texto "22" → 22.0
        except ValueError:                                # Línea 45: Si falla (ej. "abc" no es número)...
            continue                                      # Línea 46: ...ignora la línea

        if unidad == 'F':                                 # Línea 48: Si la unidad es Fahrenheit...
            celsius = fahrenheit_a_celsius(temp)          # Línea 49: ...convierte a Celsius usando la función
        else:                                             # Línea 50: Si ya es Celsius...
            celsius = temp                                # Línea 51: ...la usa directamente

        clasificacion = clasificar(celsius)               # Línea 53: Obtiene la categoría según la temperatura
        print(f"{ciudad},{celsius:.1f},{clasificacion}")  # Línea 54: Imprime la línea de salida con 1 decimal

if __name__ == "__main__":   # Línea 56: Verifica que el script se ejecuta directamente (no importado)
    main()                   # Línea 57: Llama a la función principal
