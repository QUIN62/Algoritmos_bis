def mango(quantity, price):
    # Calcular la cantidad de mangos que se deben pagar (cada 3 mangos, pagas 2)
    paid_mango_count = quantity - (quantity // 3)
    # Calcular el costo total
    total_cost = paid_mango_count * price
    return total_cost

# Ejemplo de uso
print(mango(2, 3))  # Salida: 6
print(mango(3, 3))  # Salida: 6
print(mango(5, 3))  # Salida: 12
print(mango(9, 5))  # Salida: 30
