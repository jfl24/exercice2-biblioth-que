# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur):
    bibliotheque.append({"titre": titre, "auteur": auteur})
    return bibliotheque

def afficher_livres():
    for livre in bibliotheque:
        print(f'{livre["auteur"]}:{livre["titre"]}---{livre["année"]}')

afficher_livres()