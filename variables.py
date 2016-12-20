#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# les variables couleurs
fond = (0, 0, 25)
red = (255, 0, 0)
violet = (3, 34, 75)
green = (0, 255, 0)
white = (255, 255, 255)
blue = (0, 0, 128)
yellow = (255, 255, 0)
tomato = (255, 99, 71)
hotpink = (255, 105, 180)
violetred = (208, 32, 144)
darkorange = (255, 140, 0)
chocolate = (255, 127, 36)
medium = (186, 85, 211)

#liste couleurs aléatoires
liste_couleurs = [red, green, white, yellow, tomato, hotpink, violetred, darkorange, chocolate, medium]

#Liste des tetris
tetries = []

#initialisation des variables
point = 0
case_largeur = 10
case_hauteur = 2 * case_largeur + 2
cote_tetri = 3 * case_largeur
largeur_rectangle = cote_tetri * case_largeur
espace = largeur_rectangle
largeur_fenetre = largeur_rectangle + espace
hauteur = cote_tetri * case_hauteur

#les variables du tetriminos qui descend et et celui qui est immobile
immobiles = []   # [[x, y], [x1, y2] ]
bouge = None