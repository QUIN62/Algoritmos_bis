def calculate_pet_years(human_years):
    # Inicializar las variables para los años de gato y perro
    cat_years = 0
    dog_years = 0

    # Calcular los años de gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calcular los años de perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Ejemplo de uso
print(calculate_pet_years(1))  # Salida: [1, 15, 15]
print(calculate_pet_years(2))  # Salida: [2, 24, 24]
print(calculate_pet_years(3))  # Salida: [3, 28, 29]
