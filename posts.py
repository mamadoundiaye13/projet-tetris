#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#importation des modules necessaires
import pygame
from pygame.locals import *
from variables import *

pygame.init()  #initialisaiton de pygame

#on cree la fenetre
fenetre = pygame.display.set_mode((largeur_fenetre,hauteur)) 
pygame.display.set_caption("GAME-TETRIS") #le nom de la fenetre

pygame.key.set_repeat(1, 500)

#creation du tetrimino
carre = pygame.Surface((cote_tetri,cote_tetri))
pygame.draw.rect(carre, white, (0, 0,cote_tetri, cote_tetri))

#surface de jeu
aire = pygame.Surface((espace,hauteur))
pygame.draw.rect(aire, violet, (0, 0, espace, hauteur))

#fonction qui cree la surface pour ecrire
def creer_texte (texte, font):
    Surface = font.render(texte,True,white)
    return Surface, Surface.get_rect()

#fonction pour ecrire
def message_titre (texte):
    titre = pygame.font.SysFont("Serif", 4*case_largeur)
    titreSurf, titreRect = creer_texte (texte, titre)
    titreRect.center = (espace/2), (espace/2 - 5*case_hauteur)
    aire.blit(titreSurf, titreRect)

def message_score (texte):
    score = pygame.font.SysFont("Arial", 4*case_largeur)
    scoreSurf, scoreRect = creer_texte (texte, score)
    scoreRect.center = (espace/2 -5*case_largeur), ((espace/2) + 5*case_hauteur)
    aire.blit(scoreSurf, scoreRect)

def message_niveau (texte):
    niveau = pygame.font.SysFont("Arial", 4*case_largeur)
    niveauSurf, niveauRect = creer_texte (texte, niveau)
    niveauRect.center = ((espace/2) - 5*case_largeur), ((espace/2) )
    aire.blit(niveauSurf, niveauRect)
    pygame.display.update()

def message_welcome (texte):
    fin = pygame.font.SysFont("Arial", 4*case_largeur)
    finSurf, finRect = creer_texte (texte, fin)
    finRect.center = ((espace/2) + 15*case_largeur), ((espace/2) )
    fenetre.blit(finSurf, finRect)

    entrer = pygame.font.SysFont("Arial", 2*case_largeur)
    entrerSurf, entrerRect = creer_texte ("APPUYER SUR ENTRER POUR JOUER  !", entrer)
    entrerRect.center = ((espace/2) + 15*case_largeur), ((espace/2) + 7*case_hauteur )
    fenetre.blit(entrerSurf, entrerRect)

    echap = pygame.font.SysFont("Arial", 2*case_largeur)
    echapSurf, echapRect = creer_texte ("APPUYER SUR ECHAP POUR QUITTER  !", echap)
    echapRect.center = ((espace/2) + 15*case_largeur), ((espace/2) + 10*case_hauteur )
    fenetre.blit(echapSurf, echapRect)
    pygame.display.update()

#la fonction de la surface violet
def rectangle(bouge,aire):
    fenetre.blit(aire, (case_largeur * cote_tetri, 0))

 #la fonction de la surface du tetrimino blanc
def tetrimino(x,y,image):
    fenetre.blit(image, (x,y))

#creation de la fenetre menu
def  Menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    menu = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
        fenetre.fill(green)
        message_welcome("WELCOME TO GAME-TETRIS")
        pygame.display.flip()
        
#creation de la fenetre game_over        
def  OVER():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                quit()
        fond = pygame.image.load("photo.jpg").convert()
        fenetre.blit(fond, (0,0))
        pygame.display.flip()
        

