# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur, année):
    bibliotheque.append({"titre": titre, "auteur": auteur, "année": année})
    return bibliotheque

def afficher_livres():
    for livre in bibliotheque:
        print(f'{livre["auteur"]}:{livre["titre"]}---{livre["année"]}')

afficher_livres()