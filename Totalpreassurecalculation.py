"""hola """
def total_pressure(M1, M2, m1, m2, V, T):
    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15
    # Constante de gas
    R = 0.082

    # Calcular la presión total usando la fórmula dada
    P_total = (m1 / M1 + m2 / M2) * R * T_kelvin / V

    return P_total


# Ejemplo de uso
print(total_pressure(32, 28, 16, 14, 1, 25))  # Ajusta los valores según necesites
