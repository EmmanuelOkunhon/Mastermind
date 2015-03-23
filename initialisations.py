import random

def saisir_entier(phrase1,phrase2):
    parametre=0
    temp = input(phrase1)
    try:
        parametre = eval(temp)
    except:
        pass
    while (not isinstance(parametre, int))or parametre<=0:
        temp = input(phrase2)
        try:
            parametre = eval(temp)
        except:
            pass
    return parametre

def parametres():
    return (saisir_entier("Saisir le nombre de couleurs : ","Saisir un nombre valide de couleurs (nombre entier positif non nul) : "),
            saisir_entier("Saisir la longueur de la suite à deviner : ","Saisir une longueur valide de la suite à deviner (nombre entier positif non nul) : "),
            saisir_entier("Saisir le nombre d'essais : ","Saisir un nombre valide d'essais (nombre entier positif non nul) : "))
    # si vous avez rentré autre chose qu'un nombre entier, le programme vous demandera d'en rentrer un non nul.

def ligne(couleurs,longueur):
    liste = []
    while len(liste)<longueur:
        liste.append(random.randrange(1,couleurs+1))
    return liste
