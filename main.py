

#importation des modules necessaires
import pygame
from pygame.locals import *
from variables import * #importation du fichier variables
from posts import *     #importation du fichier posts
from parameter import * #importation du fichier parameter

son = pygame.mixer.Sound("Tetris.ogg") # implentation du son

son.play()        
Menu()
principale()
pygame.quit()
quit()
