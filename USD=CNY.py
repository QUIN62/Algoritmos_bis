def convert_usd_to_cny(usd):
    # Tasa de conversión
    conversion_rate = 6.75
    # Convertir a CNY
    cny = usd * conversion_rate
    # Formatear el resultado con 2 decimales
    return f"{cny:.2f} Chinese Yuan"

# Ejemplo de uso
print(convert_usd_to_cny(15))   # Salida: '101.25 Chinese Yuan'
print(convert_usd_to_cny(465))  # Salida: '3138.75 Chinese Yuan'
