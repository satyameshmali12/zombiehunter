# creating the playing screen it will be further used in the main.py where the main game is running
import pygame
import sys

def playing(display):
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            sys.exit()


    display.fill("white")