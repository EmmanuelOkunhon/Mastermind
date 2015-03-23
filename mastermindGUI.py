import pygame,sys,tourDeJeu,initialisations,os

Gris = (200,200,200)
Blanc = (255,255,255)
Noir = (0,0,0)
Bleu = (0,0,255)
Vert = (0,255,0)
Rouge = (255,0,0)
Orange = (255,127,39)
Jaune = (250,219,5)
Rose = (255,128,192)
dict_couleurs = {1:Bleu , 2:Vert, 3:Rouge, 4:Orange , 5:Jaune, 6:Rose}
fenêtre = pygame.display.set_mode((650,770))
pygame.display.set_caption("Mastermind Mini-Projet 1ADS")
boutons = {}
gagne = False
pouce_victoire = pygame.image.load('pouce_victoire.jpg')
pouce_defaite = pygame.image.load('pouce_defaite.jpg')
son = 0
son2 = 0

def initialisation_fenetre():
    # Affichage de la fenêtre
    pygame.init()
    # Dessin du rectangle
    pygame.draw.rect(fenêtre,Gris,(60,85,301,501))
    # Affichage des couleurs de choix
    for couleur,i in [(Bleu,86),(Rouge,136),(Vert,186),(Orange,236),(Jaune,286),(Rose,336)]:
        pygame.draw.circle(fenêtre,couleur,(i,40),14)
    # Affichage des lignes verticales pour quadrillage
    for i in range(5):
        pygame.draw.line(fenêtre,Noir,(111+(i*50),85),(111+(i*50),600),1)
    # Affichage des lignes horizontales pour quadrillage
    for i in range(9):
        pygame.draw.line(fenêtre,Noir,(60,135+(i*50)),(361,135+(i*50)),1)
    # Affichage des points noirs pour ancrage des couleurs
    for i in range(4):
        # Points de solutions
        pygame.draw.circle(fenêtre,Noir,(136+(i*50),681),14)
        pygame.draw.circle(fenêtre,Blanc,(136+(i*50),681),5)
        for j in range(109,560,50):
            # Points d'essais
            pygame.draw.circle(fenêtre,Noir,(136+(i*50),j),5)
    # Affichage des points de verification
    for i in [325,348]:
        for j in range(100,551,50):
            pygame.draw.circle(fenêtre,Noir,(i,j),5)
            pygame.draw.circle(fenêtre,Noir,(i,j+23),5)
    # Textes de la fenetre
    ecriture = pygame.font.Font("freesansbold.ttf",20)
    for i,texte in [(50,"Tester la ligne"),(100,"Effacer la ligne"),
                   (150,"Sauvegarder"),(200,"Charger une partie"),(250,"Recommencer")]:
        texteSurface = ecriture.render(texte,True,Blanc,Noir)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (450,i)
        fenêtre.blit(texteSurface,texteRect)
        boutons[texte]=texteRect
    texteSurface = ecriture.render("Solution :",True,Blanc,Noir)
    texteRect = texteSurface.get_rect()
    texteRect.bottomleft = (10,690)
    fenêtre.blit(texteSurface,texteRect)
    # Affichage des numeros de lignes
    for i in range(101,552,50):
        texteSurface = ecriture.render(str(int((i-51)/50)),True,Noir)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (80,i)
        if i == 551:
            texteRect.topleft = (75,i)
        fenêtre.blit(texteSurface,texteRect)
    # Suppression des champs gagne et perdu
    resultat(True,Noir)
    resultat(color=Noir)
    # Son pour les résultats
    global son
    global son2
    son = pygame.mixer.Sound("son_victoire.wav")
    son2 = pygame.mixer.Sound("wrong_buzzer.wav")

def charger_lignes(liste_combinaisons,liste_resultats,ligne_courante):
    for ligne in liste_combinaisons:
        for circle in ligne:
            couleur,x,y = circle
            pygame.draw.circle(fenêtre,couleur,(x,y),14)
    for index in range(len(liste_resultats)):
        affichage_resultats(liste_resultats[index][0],liste_resultats[index][1],index+1)
    for circle in ligne_courante:
        couleur,x,y = circle
        pygame.draw.circle(fenêtre,couleur,(x,y),14)

def affichage_resultats(bien_places,mal_places,essais):
    if bien_places == 4:
        global gagne
        gagne = True
    liste = bien_places*[Rouge]+mal_places*[Blanc]
    for index in range(len(liste)):
        j,i = 325, (essais-1)*50+100
        # Organisation des points de verification
        # selon un quadrillage 2x2
        if index%2 == 1:
            j += 23
        if index // 2 ==1:
            i += 23
        # Affichage des pions de placement
        pygame.draw.circle(fenêtre,liste[index],(j,i),5)

def resultat(gagne=False,color = Blanc):
    ecriture = pygame.font.Font("freesansbold.ttf",40)
    if gagne:
        texteSurf = ecriture.render("GAGNE !",True,color,Noir)
    else:
        texteSurf = ecriture.render("PERDU !",True,color,Noir)
    texteRectangle = texteSurf.get_rect()
    texteRectangle.topleft = (450,400)
    fenêtre.blit(texteSurf,texteRectangle)

def afficher_solution(combinaison):
    for i in range(4):
        # Points de solutions
        pygame.draw.circle(fenêtre,combinaison[i],(136+(i*50),681),14)

def sauvegarder(combinaison_ordinateur, liste_lignes, liste_resultats, ligne_courante):
    output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'save.txt'),"w")
    output.write(str(combinaison_ordinateur)+'\n')
    output.write(str(liste_lignes)+'\n')
    output.write(str(liste_resultats)+'\n')
    output.write(str(ligne_courante)+'\n')
    output.close()

def charger_partie():
    input = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'save.txt'),"r")
    liste = input.readlines()
    input.close()
    fenetre_de_jeu(eval(liste[0]),eval(liste[1]),eval(liste[2]),eval(liste[3]))



def fenetre_de_jeu(combinaison_ordinateur = None, liste_lignes = [], liste_resultats = [], ligne_courante = []):
    # Initialisation de la fenetre
    initialisation_fenetre()
    # Determination de la combinaison a deviner
    if combinaison_ordinateur == None:
        combinaison_ordinateur = [dict_couleurs[numero] for numero in initialisations.ligne(6,4)]
    print(combinaison_ordinateur)
    #Procédures de jeu
    if liste_lignes != []:
        essai = len(liste_lignes)
        charger_lignes(liste_lignes,liste_resultats,ligne_courante)
    else:
        essai=0
    if ligne_courante!=[]:
        position = len(ligne_courante)
    else:
        position=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = event.pos
                positions_couleurs = [(72,Bleu),(122,Rouge),(172,Vert),(222,Orange),(272,Jaune),(322,Rose)]
                for i,couleur in positions_couleurs:
                    if (position<4) and (x in range(i,i+51)) and (y in range(26,55) and essai<10):
                        pygame.draw.circle(fenêtre,couleur,(136+(position*50),109+(50*essai)),14)
                        ligne_courante.append((couleur,136+(position*50),109+(50*essai)))
                        position+=1
                for key in boutons.keys():
                    if (x in range(boutons[key].left,boutons[key].right))\
                            and (y in range(boutons[key].top,boutons[key].bottom)):
                        if key == "Recommencer":
                            global gagne
                            gagne = False
                            fenêtre.fill(Noir)
                            fenetre_de_jeu(None,[],[],[])
                        elif key == "Effacer la ligne":
                            fenetre_de_jeu(combinaison_ordinateur,liste_lignes,liste_resultats,[])
                        elif key == "Tester la ligne" and position == 4:
                            essai+=1
                            position=0
                            liste_lignes.append(ligne_courante)
                            bien, mal = tourDeJeu.verification([element[0] for element in ligne_courante],combinaison_ordinateur)
                            liste_resultats.append((bien,mal))
                            affichage_resultats(bien,mal,essai)
                            ligne_courante = []
                            if gagne:
                                resultat(True)
                                afficher_solution(combinaison_ordinateur)
                                fenêtre.blit(pouce_victoire,(450,500))
                                son.play()
                            elif essai==10:
                                resultat()
                                afficher_solution(combinaison_ordinateur)
                                fenêtre.blit(pouce_defaite,(450,500))
                                son2.play()
                        elif key == "Sauvegarder":
                            sauvegarder(combinaison_ordinateur,liste_lignes,liste_resultats,ligne_courante)
                        elif key == "Charger une partie":
                            charger_partie()
        pygame.display.update()

fenetre_de_jeu()
