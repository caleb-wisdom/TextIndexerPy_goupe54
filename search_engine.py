# Rechercher un seul mot dans l'index
def recherche_mot(index, mot):
    return index.get(mot, {})

# Rechercher plusieurs mots-clés et calculer leur score de présence
def recherche_mots(index, mots):
    resultat = {}
    for mot in mots:
        occurences = index.get(mot, {})
        for doc_id, positions in occurences.items():
            if doc_id not in resultat:
                resultat[doc_id] = 0
            resultat[doc_id] += len(positions)
    return resultat

            

