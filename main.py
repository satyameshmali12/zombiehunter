import os
import random
import sys
import pygame # importing the pygame module over here
from screens.home import home
from screens.playing import playing



# initializiing the pygame
pygame.init()

# declaring the global variable over here
width = 1200
height = 700

# creating the display over here
display = pygame.display.set_mode((width,height))
pygame.display.set_icon(pygame.image.load("sprites/back/icon.jpg"))
clock = pygame.time.Clock()


fps = 30

# data = os.read("")
data = open("data")
print(data.readlines())

if __name__ == "__main__":
    def gameloop():
        
        place = "home"

        # creating all the variables for creating a leaf falling effect
        leaflist = []
        leaflistlength = 10
        leaffall = True
        lightgreen = (50,205,50)

        # here variables for home screen

        zombiescreencount = 0
        # position of the both the zombies
        zombie1x = 10
        zombie2x = width - 30
        # speed of both the zombie it will also give the directions to the zombie
        zombie1xspeed = 3
        zombie2xspeed = -3
        playbutton = pygame.transform.scale(pygame.image.load("sprites/gui/Play (4).png"),(130,130))
        buttonx = 550
        buttony = 240

        
        # here variables for the game_over screen





        # here varibles for the game screen

        # the initail player will be
        player = "sprites/ninja"
        currentmove = "idle"
        #  here 0 = left and 1 = right
        health = 100
        direction = 1
        playerx = 20
        playery = height-360
        playerxspeed = 0
        playeryspeed = 0
        rodespeed = 10
        movecount = 0
        jumped = False
        throwing = False
        throwx = 0
        throwy = 0
        rodedirection = 0

        zombieslist = []
        zombiecount = 1




        while True:

            # making the hove screen here

            if place == "home":
                
                if zombie1x<10:
                    zombie1xspeed=3

                if zombie1x>width-100:
                    zombie1xspeed=-3
                
                if zombie2x<10:
                    zombie2xspeed=3

                if zombie2x>width-100:
                    zombie2xspeed=-3
                    
                fps = 20

                zombiescreencount,zombie1x,zombie2x,place = home(display,zombiescreencount,zombie1x,zombie2x,zombie1xspeed,zombie2xspeed,place)
                
            elif place == "game_over":
                pass

            # condition while playing the game

            elif place == "start_game":

                if zombiecount>len(zombieslist):
                    obj = {
                        "zombiex":width+random.randint(0,100),
                        "zombiey":height-360,
                        "currentmove":"run",
                        "direction":0,
                        "health":100
                    }
                    zombieslist.append(obj)

                fps = 35
                leaffall = False
                leaflistlength = 0

                # taking all the values from the playing function 
                currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist = playing(display,player,currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist)
            

            if leaffall:
                removelist = []

                if len(leaflist)<leaflistlength:
                    x = random.randint(30,width-10)
                    obj = {
                        "leafx":x,
                        "leafy":0
                    }
                    leaflist.append(obj)
                
                for i in range(len(leaflist)):
                    pygame.draw.circle(display, lightgreen, (leaflist[i]["leafx"],leaflist[i]["leafy"]), 4)
                    leaflist[i].update({
                        "leafx":leaflist[i]["leafx"]+2,
                        "leafy":leaflist[i]["leafy"]+2
                    })
                    if leaflist[i]["leafx"]>width or leaflist[i]["leafx"]<0 or leaflist[i]["leafy"]>height:
                        removelist.append(i)
                
                for i in range(len(removelist)):
                    leaflist.remove(leaflist[removelist[i]])




            pygame.display.update()

            clock.tick(fps)
                



    gameloop()
