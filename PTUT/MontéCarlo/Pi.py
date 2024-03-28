import random

def approximer_pi_monte_carlo(nombre_de_points):
    """
    Approxime la valeur de PI en utilisant la méthode de Monte Carlo.

    :param nombre_de_points: Le nombre de points à générer pour l'approximation.
    :return: L'approximation de PI.
    """
    points_dans_cercle = 0

    for _ in range(nombre_de_points):
        # Générer un point aléatoire (x, y) dans le carré [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Vérifier si le point est à l'intérieur du quart de cercle
        if x**2 + y**2 <= 1:
            points_dans_cercle += 1

    # Approximer PI en utilisant la proportion de points à l'intérieur du cercle
    return 4 * points_dans_cercle / nombre_de_points

# Exemple d'utilisation
nombre_de_points = 100000  # Plus ce nombre est élevé, plus l'approximation est précise
approximation_de_pi = approximer_pi_monte_carlo(nombre_de_points)
print(f"L'approximation de PI avec {nombre_de_points} points est: {approximation_de_pi}")
