import initialisations,tourDeJeu

def masterMind():
    constantes = initialisations.parametres()
    combinaison = initialisations.ligne(constantes[0],constantes[1])
    for essai in range(constantes[2]):
        print("\nessai %s"% (essai+1))
        proposition = tourDeJeu.choix(constantes[0],constantes[1])
        verification = tourDeJeu.verification(proposition,combinaison)
        tourDeJeu.resultat_1(verification[0],verification[1])
        if verification[0] == constantes[1]:
            print("Gagné, vous avez bien trouvé : ",end = "")
            tourDeJeu.resultat_2(combinaison)
            return
    print("Perdu, il fallait trouver : ",end = "")
    tourDeJeu.resultat_2(combinaison)

masterMind()
