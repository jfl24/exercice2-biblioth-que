# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur, année):
    bibliotheque.append({
        "titre": titre,
        "auteur": auteur,
        "année": année
    })
    return bibliotheque

def afficher_livres():
    for livre in bibliotheque:
        print(f'{livre["auteur"]}:{livre["titre"]}---{livre["année"]}')

def rechercher_livre(titre):
    resultats = [
        livre for livre in bibliotheque
        if livre["titre"].lower() == titre.lower()
    ]
    if resultats:
        print("Livre(s) trouvé(s) :")
        for livre in resultats:
            print(f'- {livre["titre"]} par {livre["auteur"]} ({livre["année"]})')
        return True
    else:
        print("Aucun livre trouvé avec ce titre.")
        return False

def test_ajouter_livre():
    bibliotheque.clear()
    ajouter_livre("1984", "George Orwell", 1949)
    assert len(bibliotheque) == 1
    assert bibliotheque[0]["titre"] == "1984"
    assert bibliotheque[0]["auteur"] == "George Orwell"

def test_afficher_livres():
    bibliotheque.clear()
    ajouter_livre("Dune", "Frank Herbert", 1965)
    print("Affichage des livres :")
    afficher_livres()

def test_rechercher_livre():
    bibliotheque.clear()
    ajouter_livre("Python", "Guido", 1991)
    assert rechercher_livre("Python") is True
    assert rechercher_livre("Java") is False


if __name__ == "__main__":
    test_ajouter_livre()
    test_afficher_livres()
    test_rechercher_livre()
    print("Tous les tests ont réussi !")
