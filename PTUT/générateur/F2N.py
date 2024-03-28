def lfsr(seed, taps):
    """
    Génèreur basé sur un LFSR (Linear Feedback Shift Register).
    
    :param seed: État initial du LFSR (entier ou séquence de bits).
    :param taps: Positions des bits qui contribuent au bit de feedback.
    """
    state = seed
    while True:
        # Calculer le bit de feedback comme le XOR des bits sélectionnés par taps
        feedback = 0
        for t in taps:
            feedback ^= (state >> t) & 1
        # Décaler les bits d'un cran vers la droite et insérer le bit de feedback
        state = (state >> 1) | (feedback << (len(bin(seed)) - 3))
        yield state

# Exemple d'utilisation
if __name__ == "__main__":
    seed = 0b11001010  # État initial (ex. 202 en base 10)
    taps = [7, 5, 4, 3]  # Polynôme de rétroaction x^8 + x^6 + x^5 + x^4 + x^3 + 1

    generator = lfsr(seed, taps)
    
    # Générer 10 états pseudo-aléatoires
    for _ in range(10):
        print(format(next(generator), '08b'))

