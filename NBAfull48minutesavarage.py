def nba_extrap(ppg, mpg):
    if ppg == 0 or mpg == 0:
        return 0
    # Calcular ppg extrapolado para 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48
    # Redondear a la décima más cercana
    return round(extrapolated_ppg, 1)

# Ejemplo de uso
print(nba_extrap(12, 20))  # Salida: 28.8
print(nba_extrap(10, 10))  # Salida: 48
print(nba_extrap(5, 17))   # Salida: 14.1
print(nba_extrap(0, 0))    # Salida:
