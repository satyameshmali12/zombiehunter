import os
import sys
import pygame # importing the pygame module over here
from screens.home import home


from resources.functions import loadimage,displayimage,displaytext,scaleimage,listallthefiles

# background = scaleimage(loadimage("sprites/back/background.webp"),1200,700)
# zombiefdead = listallthefiles("sprites/zombie/female/dead")


# initializiing the pygame
pygame.init()

# declaring the global variable over here
width = 1200
height = 700

# creating the display over here
display = pygame.display.set_mode((width,height))
pygame.display.set_icon(pygame.image.load("sprites/back/icon.jpg"))
clock = pygame.time.Clock()

fps = 15

# data = os.read("")
data = open("data")
print(data.readlines())

if __name__ == "__main__":
    def gameloop():
        
        place = "home"

        # here variables for home screen
        zombiescreencount = 0
        zombie1x = 10
        zombie2x = width - 10

        
        # here variables for the game_over screen



        # here varibles for the game screen

        while True:

            # to quit the game
            for e in pygame.event.get():
                    if e.type==pygame.QUIT:
                        sys.exit()

            # making the hove screen here

            if place == "home":

                fps = 12

                zombiescreencount,zombie1x,zombie2x = home(display,zombiescreencount,zombie1x,zombie2x)
                

            elif place == "game_over":
                pass

            else:
                pass

            pygame.display.update()

            clock.tick(fps)
                



    gameloop()

