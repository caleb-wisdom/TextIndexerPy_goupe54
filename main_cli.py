import os
from document_loader import charger_documents, preparer_documents
from indexer import construire_index_inverse
from search_engine import recherche_mots
from retrieval import trier_documents, extraire_snippets
from stats import calculer_statistiques

# interface utilisateur en ligne de commande
def main():
   # dossier = input("Entrez le chemin du dossier contenant les fichiers texte : ")
    documents = charger_documents('textes')
    documents_tokens = preparer_documents(documents)
    index, tf = construire_index_inverse(documents_tokens)

    while True:
        choix = input("\n1. Rechercher\n2. Statistiques\n3. Quitter\n> ")

        if choix == "1":
            requete = input("Entrez les mots-clés : ").lower().split()
            resultats = recherche_mots(index, requete)
            if not resultats:
                print("Aucun document ne contient les mots-clés fournis.")
            else:
                tries = trier_documents(resultats)
                for doc_id, score in tries:
                    print(f"{doc_id} (score : {score})")
                    for extrait in extraire_snippets(documents, doc_id, requete):
                        print(f"  ...{extrait}...")

        elif choix == "2":
            stats = calculer_statistiques(documents_tokens)
            print(f"Documents analysés : {stats['nb_docs']}")
            print(f"Nombre total de mots : {stats['nb_mots_total']}")
            print(f"Nombre de mots uniques : {stats['nb_mots_uniques']}")
            print("Mots les plus fréquents :")
            for mot, freq in stats["mots_frequents"]:
                print(f"  {mot} : {freq}")

        elif choix == "3":
            break

if __name__ == "__main__":
    main()
