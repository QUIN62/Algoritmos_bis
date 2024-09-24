import math

def convert_to_16_9(x, y):
    # Calcular la nueva resolución X manteniendo la altura
    new_x = math.ceil((16 / 9) * y)
    return new_x, y

# Ejemplo de uso
print(convert_to_16_9(374, 280))  # Salida: (498, 280)
print(convert_to_16_9(500, 280))  # Salida: (498, 280)
