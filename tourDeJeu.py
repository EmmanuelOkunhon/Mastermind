def choix(couleurs,longueur,texte="saisir votre proposition : "):
    liste = list(input(texte))
    if len(liste) != longueur:
        return choix(couleurs,longueur,"saisir une proposition valide : ")
    for i in range(len(liste)):
        try:
            liste[i] = eval(liste[i])
            if liste[i] not in range(1,couleurs+1):
                return choix(couleurs,longueur,"saisir une proposition valide : ")
        except:
            return choix(couleurs,longueur,"saisir une proposition valide : ")
    return liste

def verification(joueur,ordinateur):
    mauvais_joueur = []
    mauvais_ordinateur = []
    bien_places = 0
    for index in range(len(joueur)):
        if joueur[index] == ordinateur[index]:
            bien_places += 1
        else:
            mauvais_joueur.append(joueur[index])
            mauvais_ordinateur.append(ordinateur[index])
    mal_places = 0
    for element in mauvais_joueur:
        if element in mauvais_ordinateur:
            mal_places += 1
    return bien_places,mal_places

def resultat_1(bien_places,mal_places):
    print("%s bien placé(s), et %s mal placé(s)" %(bien_places,mal_places))

def resultat_2(entiers):
    resultat = ""
    for entier in entiers:
        resultat+=str(entier)
    print(resultat)