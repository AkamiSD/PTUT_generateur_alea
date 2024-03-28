def lfsr(seed, taps, length):
    """
    Un générateur simple de LFSR (registre à décalage à rétroaction linéaire).
    
    :param seed: État initial du LFSR, utilisé comme point de départ pour la génération.
    :param taps: Les positions qui contribuent au bit de feedback, basées sur le polynôme de rétroaction.
    :param length: Nombre de bits à générer.
    :return: Génère un bit à chaque itération.
    """
    state = seed
    for _ in range(length):
        # Calcul du bit de feedback à partir des positions spécifiées dans taps
        feedback = 0
        for t in taps:
            feedback ^= (state >> t) & 1
        # Mise à jour de l'état en décalant et en ajoutant le bit de feedback à la fin
        state = (state >> 1) | (feedback << (len(bin(seed)) - 3))
        # Retourne le bit le plus à droite de l'état actuel
        yield state & 1

def geffe_generator(L1_seed, L1_taps, L2_seed, L2_taps, L3_seed, L3_taps, length):
    """
    Génère une séquence pseudo-aléatoire en utilisant le générateur Geffe.
    
    :param L1_seed, L2_seed, L3_seed: États initiaux pour les trois LFSRs.
    :param L1_taps, L2_taps, L3_taps: Configurations des taps pour chaque LFSR.
    :param length: Longueur de la séquence à générer.
    :return: Génère un bit de la séquence pseudo-aléatoire à chaque itération.
    """
    # Initialisation des trois LFSRs avec leurs états initiaux et configurations de taps
    L1 = lfsr(L1_seed, L1_taps, length)
    L2 = lfsr(L2_seed, L2_taps, length)
    L3 = lfsr(L3_seed, L3_taps, length)

    for _ in range(length):
        # Lecture d'un bit de chaque LFSR
        L1_bit = next(L1)
        L2_bit = next(L2)
        L3_bit = next(L3)
        # Combinaison des bits en utilisant la logique spécifique au générateur Geffe
        yield (L1_bit & L2_bit) ^ ((1 - L1_bit) & L3_bit)

# Exemple d'utilisation
if __name__ == "__main__":
    length = 10  # Nombre de bits à générer
    # Appel du générateur Geffe avec les configurations spécifiques pour chaque LFSR
    sequence = geffe_generator(
        L1_seed=0b001, L1_taps=[2, 1], # 0b001 indique le fait d'être en base deux 001 = 1
        L2_seed=0b010, L2_taps=[2, 1], #  010 = 2
        L3_seed=0b100, L3_taps=[2, 1], #  100 = 4
        length=length
    )

    # Affichage de la séquence générée
    for bit in sequence:
        print(bit, end='')
