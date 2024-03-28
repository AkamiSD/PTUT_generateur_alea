def linear_algebra_rng(seed, n):
    numbers = []  # Liste pour stocker les nombres générés
    current_state = seed  # Initialisation avec la graine

    for _ in range(n):
        # Transformation linéaire : XOR avec une permutation de l'état actuel
        current_state ^= (current_state << 13)
        current_state ^= (current_state >> 17)
        current_state ^= (current_state << 5)
        
        # Ajouter le nombre généré à la liste
        numbers.append(current_state)

    return numbers

# Exemple d'utilisation :
seed = 11001010111111101011101010111110  # Graine initiale
n = 3  # Nombre de nombres pseudo-aléatoires à générer
random_numbers = linear_algebra_rng(seed, n)
print(random_numbers)

#11001010111111101011101010111110
#3405691582
#0xCAFEBABE

#[900213096610090, 233808968564365520084, 61839866800683197647603492]
