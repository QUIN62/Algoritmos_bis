"""hi"""
import math


def age_range(n):
    if n <= 14:
        min_age = math.floor(n - 0.10 * n)
        max_age = math.floor(n + 0.10 * n)
    else:
        min_age = math.floor(n / 2 + 7)
        max_age = math.floor((n - 7) * 2)

    return f"{min_age}-{max_age}"


# Ejemplo de uso
print(age_range(27))  # Salida: '20-40'
print(age_range(5))  # Salida: '4-5'
print(age_range(17))  # Salida: '15-20'
print(age_range(14))  # Salida: '12-15'
