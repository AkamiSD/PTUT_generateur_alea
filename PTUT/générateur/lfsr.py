def lfsr(seed, taps, steps):
    """
    Génère une séquence de nombres pseudo-aléatoires avec un LFSR.

    :param seed: La valeur initiale (graine) du LFSR, doit être non-nulle.
    :param taps: Les positions des bits utilisés pour le calcul du feedback XOR.
    :param steps: Le nombre de bits à générer.
    :return: Génère chaque bit de la séquence.
    """
    state = seed
    n_bits = seed.bit_length()  # Détermine la longueur de la graine en bits

    for _ in range(steps):
        # Calcul du bit de feedback en appliquant XOR aux bits sélectionnés par taps
        feedback = 0
        for t in taps:
            feedback ^= (state >> (n_bits - 1 - t)) & 1
        
        # Décale l'état d'un bit vers la gauche et ajoute le feedback à la droite
        state = (state << 1) & ((1 << n_bits) - 1)  # Garde l'état dans les n_bits
        state |= feedback
        
        yield state

# Exemple d'utilisation
if __name__ == "__main__":
    seed = 0b101001  # Une graine initiale, par exemple 41 en décimal
    taps = [5, 2]  # Utilise les bits 5 (le plus à gauche) et 2 pour le feedback
    steps = 10  # Génère 10 bits

    for bit in lfsr(seed, taps, steps):
        print(bin(bit)[2:].zfill(seed.bit_length()))  # Affiche la séquence générée
