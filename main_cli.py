
import argparse
from stats import calculer_statistiques

def charger_donnees(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return f.readlines()

def afficher_stats(stats):
    for k, v in stats.items():
        print(f"{k}: {v}")

def main():
    parser = argparse.ArgumentParser(description="Calcul des statistiques sur un corpus.")
    parser.add_argument("fichier", help="Chemin vers le fichier contenant les documents")
    args = parser.parse_args()

    documents = charger_donnees(args.fichier)
    stats = calculer_statistiques(documents)
    afficher_stats(stats)

if __name__ == "__main__":
    main()

