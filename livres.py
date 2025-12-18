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

import livres 
def test_ajouter_livre():
    livres.bibliotheque.clear()  
    livres.ajouter_livre("1984", "George Orwell")
    assert len(livres.bibliotheque) == 1
    assert livres.bibliotheque[0]["titre"] == "1984"
    assert livres.bibliotheque[0]["auteur"] == "George Orwell"

def test_afficher_livres():
    livres.bibliotheque.clear()
    livres.ajouter_livre("Dune", "Frank Herbert")
    print("Affichage des livres :")
    livres.afficher_livres()  

def test_rechercher_livre():
    livres.bibliotheque.clear()
    livres.ajouter_livre("Python", "Guido")
    assert livres.rechercher_livre("Python") is True
    assert livres.rechercher_livre("Java") is False

if __name__ == "__main__":
    test_ajouter_livre()
    test_afficher_livres()
    test_rechercher_livre()
    print("Tous les tests ont réussi !")
