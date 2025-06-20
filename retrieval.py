# Trier les documents selon leur score décroissant
def trier_documents(resultats):
    return sorted(resultats.items(), key=lambda x: x[1], reverse=True)

# Extraire des extraits de texte contenant les mots-clés
def extraire_snippets(documents, doc_id, mots_cles):
    texte = documents[doc_id]
    extraits = []
    for mot in mots_cles:
        debut = texte.lower().find(mot)
        if debut != -1:
            extrait = texte[max(0, debut - 30):debut + 30]
            extraits.append(extrait)
    return extraits
