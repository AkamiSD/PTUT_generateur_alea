def von_neumann_generator(seed, n):
    """
    Génère n nombres pseudo-aléatoires en utilisant la méthode du carré du milieu de Von Neumann.

    :param seed: Un entier servant de valeur initiale (seed).
    :param n: Le nombre de nombres pseudo-aléatoires à générer.
    :return: Une liste de n nombres pseudo-aléatoires.
    """
    numbers = []  # Liste pour stocker les nombres générés
    current_number = seed  # Initialiser avec le seed

    for _ in range(n):
        squared = current_number ** 2  # Mettre au carré le nombre actuel
        str_squared = str(squared).zfill(8)  # Convertir en chaîne et ajouter des zéros au début pour avoir au moins 8 chiffres
        middle_digits = str_squared[len(str_squared)//2 - 2:len(str_squared)//2 + 2]  # Extraire les 4 chiffres du milieu
        current_number = int(middle_digits)  # Convertir en entier pour la prochaine itération
        numbers.append(current_number)  # Ajouter le nombre généré à la liste

    return numbers

# Exemple d'utilisation
seed = 7533  # Valeur initiale
n = 100  # Nombre de nombres à générer
random_numbers = von_neumann_generator(seed, n)
print(random_numbers)


