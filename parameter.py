#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#imprtation des modules necessaires
import pygame
from pygame.locals import *
from random import *
from variables import *
from posts import *



#permet d'obtenir un nouveau carré avec une couleur aléatoire dans liste_couleurs
def get_carre(cote_tetri, couleur):
    carre = pygame.Surface((cote_tetri,cote_tetri))
    pygame.draw.rect(carre, couleur, (0, 0,cote_tetri, cote_tetri))
    return carre

#on appelle les fonctions qui permettent d'ecrire sur aire
def score ():
    global point
    message_niveau("Level: 1")
    message_score("Score: " + str(point))
    message_titre("GAME-TETRIS")

#test qui supprime la ligne si elle est pleine  
def lignePleine():
    global point
    global immobiles
    lignes = {i:0 for i in range(case_hauteur)}
    for x,y in immobiles:
        lignes[y/cote_tetri] += 1
    new_immobiles = []
    combien_ligne = 0
    y_max = 0
    for l in lignes:
        if lignes[l] == case_largeur:
            combien_ligne += 1
            if y_max < l:
                y_max = l
    if combien_ligne == 0:
        return     #rien ne bouge
    for cube in immobiles:
        y_cube = cube[1] / cote_tetri
        if lignes[y_cube] != case_largeur:
            if y_cube < y_max:
                new_immobiles.append([cube[0], (y_cube + combien_ligne)*cote_tetri])
            else:
                new_immobiles.append(cube)
    immobiles = new_immobiles

    if lignePleine:  #test pour le score
        point += 40
#test qui fait game_over quand la colonne est pleine
def HauteurPleine():
    global immobiles

    lignes = {i:0 for i in range(case_hauteur)}
    for x,y in immobiles:
        lignes[x/cote_tetri] += 1
    new_immobiles = []
    combien_ligne = 0
    x_max = 0
    for l in lignes:
        if lignes[l] == case_hauteur:
            OVER()    #appel de la fonction  GAME_OVER
            if x_max < l:
                x_max = l
    if combien_ligne == 0:
        return         # rien ne bouge
    for cube in immobiles:
        x_cube = cube[1] / cote_tetri
        if lignes[x_cube] != case_hauteur:
            if x_cube < x_max:
                new_immobiles.append([cube[1], (x_cube + combien_ligne)*cote_tetri])
            else:
                new_immobiles.append(cube)
    immobiles = new_immobiles

# test si il y a une colision
def colision(bouge, dirx, diry):
    for bloc in immobiles:
        if bouge[0] + dirx * cote_tetri == bloc[0] and bouge[1] + diry * cote_tetri == bloc[1] :
            return True
    return False 

#la fonction principale 
def principale():
    global bouge
    
    game_over = False #variable de la boucle
    
    #la boucle principale
    while not game_over:
        if bouge == None:
            bouge = [int(case_largeur /2)*cote_tetri, 0]
            #on colle et on ajoute ce carré au tableau général des tetris
            tetries.append(get_carre(cote_tetri, liste_couleurs[randint(0, len(liste_couleurs) - 1)]));


        elif bouge[1] >= hauteur - cote_tetri:
            bouge[1] = hauteur - cote_tetri
            immobiles.append([bouge[0], bouge[1]])
            bouge = None    
                
        elif colision(bouge, 0, 1): #on fait la colision
            immobiles.append([bouge[0], bouge[1]])
            bouge = None

        else:
            bouge[1] += cote_tetri #on decend l'autre tetrimino

        #gestion d'evenement
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN and bouge:
                if event.key == pygame.K_UP:
                    bouge[1] -= cote_tetri
                    
                elif event.key == pygame.K_DOWN and bouge[1] < hauteur - cote_tetri and not colision(bouge, 0, 1):
                    bouge[1] += cote_tetri        

                elif event.key == pygame.K_LEFT and bouge[0] > 0 and not colision(bouge, -1, 0):
                    bouge[0] -= cote_tetri
                    
                elif event.key == pygame.K_RIGHT and bouge[0] < largeur_rectangle - cote_tetri and not colision(bouge, 1, 0):
                    bouge[0] += cote_tetri    
        fenetre.fill(fond) #on colore la fenetre

        #on parcourt le tableau des tetris et on les descend avec des couleurs aleatoires
        j = 0
        while j < len(immobiles):
            tetrimino(immobiles[j][0], immobiles[j][1], tetries[j])
            j += 1
        
        if bouge:
            tetrimino(bouge[0],bouge[1], tetries[len(tetries) - 1])

        rectangle(bouge,aire)
        pygame.display.update()
        pygame.time.wait(100)  #la vitesse de descente des tetriminos
        aire.fill(violet)

        lignePleine()
        HauteurPleine()
        score()