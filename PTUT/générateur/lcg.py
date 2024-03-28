def lcg(a, c, m, seed):
    """Génère un nombre pseudo-aléatoire en utilisant LCG.
    
    Args:
        a (int): Le multiplicateur.
        c (int): L'incrément.
        m (int): Le module.
        seed (int): La valeur initiale (graine).
        
    Yields:
        int: Le prochain nombre pseudo-aléatoire dans la séquence.
    """
    while True:  # Boucle infinie pour générer des nombres à la demande
        # Applique la formule LCG pour calculer le prochain nombre pseudo-aléatoire.
        # La formule est: X_(n+1) = (aX_n + c) mod m.
        # 'seed' contient le dernier nombre généré (ou la graine initiale pour la première itération).
        seed = (a * seed + c) % m
        yield seed  # Retourne le nombre généré et permet la reprise de la fonction ici lors du prochain appel.

# Exemple d'utilisation
if __name__ == "__main__": 
    # Paramètres du générateur congruentiel linéaire
    a = 1664525  # Multiplicateur
    c = 1013904223  # Incrément
    m = 2**32  # Module
    seed = 42  # Graine initiale

    # Crée un générateur de nombres pseudo-aléatoires avec les paramètres spécifiés
    random_generator = lcg(a, c, m, seed)

    # Générer 10 nombres pseudo-aléatoires
    for _ in range(10):
        # Obtient le prochain nombre pseudo-aléatoire du générateur et l'affiche
        print(next(random_generator))
	
