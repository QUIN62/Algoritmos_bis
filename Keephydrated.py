def water_needed(hours):
    # Calcular la cantidad de litros
    litres = hours * 0.5
    # Redondear hacia abajo y convertir a entero
    return int(litres)

# Ejemplo de uso
print(water_needed(3))    # Salida: 1
print(water_needed(6.7))  # Salida: 3
print(water_needed(11.8))
