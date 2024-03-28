def precalculate_transitions():
    """
    Précalculer toutes les transitions possibles entre les états pour la méthode du carré du milieu.
    Retourne un dictionnaire où les clés sont les états actuels et les valeurs sont les états suivants.
    """
    transitions = {}
    for i in range(10000):
        # Calculer le carré et extraire les chiffres du milieu comme dans la méthode du carré du milieu
        squared = i ** 2
        str_squared = str(squared).zfill(8)
        middle_digits = str_squared[len(str_squared)//2 - 2:len(str_squared)//2 + 2]
        next_state = int(middle_digits)
        transitions[i] = next_state
    return transitions

def find_seed_in_sequence(sequence, transitions):
    """
    Trouver le dernier état (seed) dans la séquence donnée en utilisant les transitions.
    
    :param sequence: La séquence des nombres générés à partir d'un certain seed.
    :param transitions: Le dictionnaire des transitions entre les états.
    :return: Le seed correspondant au dernier nombre de la séquence, si trouvé.
    """
    for possible_seed in transitions.keys():
        test_sequence = [possible_seed]
        for _ in range(len(sequence)-1):
            test_sequence.append(transitions[test_sequence[-1]])
        if test_sequence == sequence:
            return possible_seed
    return None

def predict_next_numbers_from_sequence(sequence, n, transitions):
    """
    Prédire les n prochains nombres à partir d'une séquence donnée de nombres générés.
    
    :param sequence: La séquence initiale de nombres à partir de laquelle prédire.
    :param n: Le nombre de nombres à prédire.
    :param transitions: Le dictionnaire des transitions entre les états.
    :return: Une liste des n prochains nombres prédits.
    """
    # Trouver le seed correspondant au dernier nombre de la séquence
    seed = find_seed_in_sequence(sequence, transitions)
    if seed is None:
        print("Impossible de trouver le seed dans la séquence donnée.")
        return []
    
    # Générer la suite de nombres à partir de ce seed
    predicted_sequence = [seed]
    for _ in range(n):
        predicted_sequence.append(transitions[predicted_sequence[-1]])
    return predicted_sequence[1:]  # Retourner la prédiction sans inclure le seed trouvé

# Précalcul des transitions comme dans l'exemple précédent
transitions = precalculate_transitions()

# Supposons que nous ayons la séquence suivante, générée précédemment
given_sequence = [7460, 6516, 4582, 9947, 9428]

# Nombre de prédictions à générer
n = 10

# Prédire les nombres suivants
predicted_numbers = predict_next_numbers_from_sequence(given_sequence, n, transitions)
print(predicted_numbers)
