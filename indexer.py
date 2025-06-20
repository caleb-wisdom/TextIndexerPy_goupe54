from collections import defaultdict

# Construire l’index inversé et les fréquences des mots
def construire_index_inverse(documents_tokens):
    index = defaultdict(lambda: defaultdict(list))
    frequences_termes = defaultdict(lambda: defaultdict(int))

    for doc_id, tokens in documents_tokens.items():
        for position, mot in enumerate(tokens):
            index[mot][doc_id].append(position)
            frequences_termes[doc_id][mot] += 1

    return index, frequences_termes
