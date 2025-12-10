# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur, année):
    bibliotheque.append({"titre": titre, "auteur": auteur, "année": année})
    return bibliotheque

def afficher_livres():
    for livre in bibliotheque:
        print(f'{livre["auteur"]}:{livre["titre"]}---{livre["année"]}')

afficher_livres()

def rechercher_livre(titre):
    resultats = [livre for livre in bibliotheque if livre['titre'].lower() == titre.lower()]
    if resultats:
        print("Livre(s) trouvé(s) :")
        for livre in resultats:
            print(f"- {livre['titre']} par {livre['auteur']} ({livre['année']})")
    else:
        print("Aucun livre trouvé avec ce titre.")