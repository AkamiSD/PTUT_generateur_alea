import numpy as np

def matrix_generator(A, seed, steps):
    """
    Cette fonction génère une séquence de vecteurs états pseudo-aléatoires
    en utilisant une matrice de transformation A sur un vecteur d'état initial.
    Les vecteurs et la matrice sont définis sur l'espace \( \mathbb{F}_2^n \),
    ce qui signifie que tous les calculs sont effectués modulo 2.

    :param A: Matrice carrée (numpy array) de taille n x n utilisée pour transformer
              l'état courant en un nouvel état. Elle doit avoir de bonnes propriétés
              algébriques pour assurer une séquence longue et apparemment aléatoire.
    :param seed: Vecteur d'état initial (liste ou numpy array) de taille n.
                 C'est le point de départ pour la génération de la séquence.
    :param steps: Le nombre d'états (vecteurs) à générer dans la séquence.
    :return: Yields un nouvel état à chaque itération, calculé en multipliant
             l'état courant par la matrice A et en prenant le résultat modulo 2.
    """
    state = np.array(seed)  # Convertit la graine initiale en un tableau numpy pour faciliter les opérations.
    for _ in range(steps):
        # Multiplie l'état courant par la matrice A et applique un modulo 2 à chaque élément du résultat.
        # Cela garantit que chaque bit de l'état suivant est soit 0, soit 1.
        state = np.dot(A, state) % 2
        yield state  # Renvoie le nouvel état calculé.

# Exemple d'utilisation
if __name__ == "__main__":
    # Définit la matrice de transformation A. Cette matrice doit être choisie soigneusement
    # pour assurer une bonne qualité de la séquence pseudo-aléatoire générée.
    A = np.array([[0, 1], [1, 1]])
    
    # Définit le vecteur d'état initial. C'est le point de départ de la séquence.
    seed = [1, 0]
    
    # Spécifie le nombre de vecteurs états à générer.
    steps = 10

    generator = matrix_generator(A, seed, steps)

    # Génère et affiche chaque nouvel état produit par le générateur.
    for state in generator:
        print(state)
