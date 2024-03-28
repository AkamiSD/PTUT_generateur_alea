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

def predict_next_numbers(seed, n, transitions):
    """
    Prédire les n prochains nombres générés par la méthode du carré du milieu, en commençant par le seed donné.
    
    :param seed: Le seed à partir duquel commencer la prédiction.
    :param n: Le nombre de prédictions à générer.
    :param transitions: Le dictionnaire des transitions entre les états.
    :return: Une liste des n prochains nombres prédits.
    """
    predicted_numbers = []
    current_state = seed
    for _ in range(n):
        current_state = transitions[current_state]
        predicted_numbers.append(current_state)
    return predicted_numbers

# Précalcul des transitions
transitions = precalculate_transitions()

# Exemple d'utilisation
seed = 7533  # Seed initial pour la prédiction
n = 5  # Nombre de prédictions à générer
predicted_numbers = predict_next_numbers(seed, n, transitions)
print(predicted_numbers)
