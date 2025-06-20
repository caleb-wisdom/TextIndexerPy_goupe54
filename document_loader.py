import os
import re

# Charger tous les fichiers texte dans un dossier donné
def charger_documents(chemin_dossier):
    documents = {}
    for nom_fichier in os.listdir(chemin_dossier):
        if nom_fichier.endswith(".txt"):
            with open(os.path.join(chemin_dossier, nom_fichier), 'r', encoding='utf-8') as fichier:
                documents[nom_fichier] = fichier.read()
    return documents

# Nettoyer un texte : mettre en minuscules, retirer ponctuation et séparer en mots
def nettoyer_texte(texte):
    texte = texte.lower()
    texte = re.sub(r'[^a-z0-9\s]', '', texte)
    mots = texte.split()
    return mots

# Appliquer le nettoyage à chaque document
def preparer_documents(documents):
    return {doc_id: nettoyer_texte(texte) for doc_id, texte in documents.items()}

