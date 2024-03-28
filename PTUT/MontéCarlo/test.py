def von_neumann_generator(seed, n):
    numbers = []
    current_number = seed
    for _ in range(n):
        squared = current_number ** 2
        str_squared = str(squared).zfill(8)
        middle_digits = str_squared[len(str_squared)//2 - 2:len(str_squared)//2 + 2]
        current_number = int(middle_digits)
        numbers.append(current_number)
    return numbers

def approximer_pi_monte_carlo_von_neumann(seed, nombre_de_points):
    points_dans_cercle = 0
    # Générer 2 * nombre_de_points parce qu'on a besoin de paires (x, y)
    random_numbers = von_neumann_generator(seed, 2 * nombre_de_points)
    
    for i in range(0, len(random_numbers), 2):
        # Normaliser les nombres pour les transformer en valeurs flottantes entre -1 et 1
        x = (random_numbers[i] % 10000) / 10000.0 * 2 - 1
        y = (random_numbers[i + 1] % 10000) / 10000.0 * 2 - 1
        
        if x**2 + y**2 <= 1:
            points_dans_cercle += 1

    return 4 * points_dans_cercle / nombre_de_points

# Exemple d'utilisation
seed = 1000
nombre_de_points = 10000
approximation_de_pi = approximer_pi_monte_carlo_von_neumann(seed, nombre_de_points)
print(f"L'approximation de PI avec {nombre_de_points} points et Von Neumann comme générateur est: {approximation_de_pi}")
