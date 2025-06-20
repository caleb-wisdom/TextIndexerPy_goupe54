from collections import Counter

# Calculer des statistiques globales sur les documents
def calculer_statistiques(documents_tokens):
    nb_docs = len(documents_tokens)
    tous_les_mots = [mot for tokens in documents_tokens.values() for mot in tokens]
    nb_mots_total = len(tous_les_mots)
    nb_mots_uniques = len(set(tous_les_mots))
    mots_frequents = Counter(tous_les_mots).most_common(10)

    return {
        "nb_docs": nb_docs,
        "nb_mots_total": nb_mots_total,
        "nb_mots_uniques": nb_mots_uniques,
        "mots_frequents": mots_frequents
    }
