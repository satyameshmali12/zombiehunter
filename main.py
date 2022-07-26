import random
import pygame
from screens.game_over import game_over # importing the pygame module over here
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


if __name__ == "__main__":
    def gameloop(location):
        
        place = location
        fps = 10

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

        
        # here variables for the game_over screen
        restart = False





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
        noofthrow = 4
        rodedirection = 0
        kills = 0
        zombieslist = []
        zombiescount = 2

        while True:

            # making the hove screen here

            if place == "home":

                try:
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
                except Exception as e:
                    print("some error occured")
                        
            elif place == "game_over":
                try:
                    leaffall=True
                    # restarting the game
                    fps = 20
                    place,restart = game_over(display,kills,place,restart)
                    if restart:
                        gameloop("start_game")

                    if place=="home":
                        gameloop("home")
                except Exception as e:
                    print("hey some error occurred")
                
                    


            # condition while playing the game

            elif place == "start_game":
                try:
                    if health<1 and currentmove=="dead" and movecount>7:
                        place="game_over"
                        pygame.mixer.music.stop()
                    if health<1:
                        currentmove="dead"

                    if zombiescount>len(zombieslist):
                        colors = ["green","yellow","blue","purple","violet"]
                        gender = random.randint(0,1)
                        gender = "male" if gender==0 else "female"
                        obj = {
                            "zombiex":width+random.randint(0,100),
                            "zombiey":height-360,
                            "currentmove":"walk",
                            "movecount":0,
                            "direction":0,
                            "health":100,
                            "gender":gender,
                            "attacking":False,
                            "speedx":random.randint(2,3),
                            "healthbarcolor":colors[random.randint(0,len(colors)-1)]
                        }
                        zombieslist.append(obj)

                    fps = 18
                    leaffall = False
                    leaflistlength = 0

                    # taking all the values from the playing function 
                    currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist,zombiescount,noofthrow,kills = playing(display,player,currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist,zombiescount,noofthrow,kills)
                except Exception as e:
                    print("some error occurred")
            

            if leaffall:
                try:
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
                except Exception as e:
                    print("some error occurred")




            pygame.display.update()

            clock.tick(fps)
                


    # running the game over here👍
    # all done enjoy

    
    gameloop("home")