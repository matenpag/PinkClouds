import pygame
clock = pygame.time.Clock()
pygame.init()
#scren 
width = 512
height = width
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pink Clouds')
Icon = pygame.image.load("Icon.png")
pygame.display.set_icon(Icon)
#variables for background variables
bgcolour = (115,170,250) 
running  = True 
pressed = False
lastPressed = 0
start_ticks = pygame.time.get_ticks()
LEFT_OF_PLAYER = 30 # the gap on the left of the player
TOP_OF_PLAYER = 96 # so that theys can be against object
#DOORS
bedDoor = False
kitchenDoor = False
hallwayBed = False
hallwayOutside = False
hallwayKitchen = False
#variables for thumbnail at start
thumbnail = pygame.image.load("Thumbnail.png")
thumbnail = pygame.transform.scale(thumbnail,(512,512))
showthumbnail = True
#help screen
helpscreen = pygame.image.load("Help Screen.PNG")
helpscreen = pygame.transform.scale(helpscreen, (512,512))
showHELP = False
#ROOMS
showBlack = False
roomName = ""

bedroom = pygame.image.load("Bedroom.png")
bedroom = pygame.transform.scale(bedroom, (512,512))
showBedroom = False

hallway1 = pygame.image.load("Hallway1.png")
hallway1 = pygame.transform.scale(hallway1,(512,512))
showHallway1 = False
hallway2 = pygame.image.load("Hallway2.png")
hallway2= pygame.transform.scale(hallway2, (512,512))
showHallway2 = False

kitchen = pygame.image.load("Kitchen.PNG")
kitchen = pygame.transform.scale(kitchen, (512,512))
showKitchen = False
#buttons
space = pygame.image.load("Space.png")
space = pygame.transform.scale(space, (128,128))
space_rect = space.get_rect(center = (width - 64, height - 32))
showSpace = True

E = pygame.image.load("E.png")
E = pygame.transform.scale(E, (64,64))
E_rectangle = E.get_rect()
showE = False
#TRYING OUT CLASSESS

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.current = 0
        self.animationSpeed = 0.2
        self.is_moving = False
        self.frames = []
        self.frames_running = []
        self.frames_runningLeft = []
        self.load_frames()
        self.direction = "right"
    def load_frames(self):
        stand_frame_names = ["Stand 01.PNG", "Stand 02.PNG", "Stand 03.PNG", 
                       "Stand 04.PNG", "Stand 05.PNG", "Stand 06.PNG", 
                       "Stand 07.PNG", "Stand 08.PNG"]
        for frame_name in stand_frame_names:
            frame = pygame.image.load(frame_name)
            frame = pygame.transform.scale(frame, (128,128))
            self.frames.append(frame)
        run_frame_names = ["Running 01.PNG", "Running 02.PNG", "Running 03.PNG", 
                           "Running 04.PNG", "Running 05.PNG", "Running 06.PNG", 
                           "Running 07.PNG", "Running 08.PNG", "Running 09.PNG", "Running 06.PNG", 
                           "Running 010.PNG", "Running 011.PNG", "Running 012.PNG"]
        for frame_name in run_frame_names:
            frame = pygame.image.load(frame_name)
            frame = pygame.transform.scale(frame, (128,128))
            self.frames_running.append(frame)
            
        for frame_name in run_frame_names:
            frame = pygame.image.load(frame_name)
            frame = pygame.transform.scale(frame, (128, 128))
            self.frames_runningLeft.append(pygame.transform.flip(frame, True, False))
    def update(self):
        if self.is_moving:
            self.current += self.animationSpeed
            if self.current >= len(self.frames_running):
                self.current = 0
        else:
            self.current += self.animationSpeed
            if self.current > len(self.frames):
                self.current = 0
    def draw(self,screen):
        if self.is_moving:
            if self.direction == "right":
                current_frame = self.frames_running[int(self.current)]
            else:
                current_frame = self.frames_runningLeft[int(self.current)]
        else:
            current_frame = self.frames[int(self.current)]
        screen.blit(current_frame, (self.x, self.y))
            
    def move(self, px, py):
        herex = self.x + px
        herey = self.y + py
        global showE # apprently python doesn't realise this isnt local (from outside)
        global bedDoor # ima take a guess and say it doesnt knwo this either
        global showHallway1, showHallway2, showBedroom, hallwayBed, hallwayOutside, kitchenDoor
        global LEFT_OF_PLAYER, TOP_OF_PLAYER, hallwayKitchen, player_rect, showKitchen #fromhereTohere

        ##BOUNDARIES##
        #scren bounds
        if not (showHallway1 or showHallway2):
            if herex < -LEFT_OF_PLAYER: #left
                herex = -LEFT_OF_PLAYER
            if self.x > width - 90: #right
                herex = width - 90
            if self.y < 120:#up
               herey = 120
            if self.y > height - 128:#down
                herey = height - 128
        elif showHallway1:
            if self.x < -LEFT_OF_PLAYER:#left
                herex = -LEFT_OF_PLAYER
            elif self.x > width - 90:#right
                herex = 32 - LEFT_OF_PLAYER
                showHallway2 = True #make variable for all rooms
                showHallway1 = False
            if self.y < 120:
               herey = 120
            if self.y > height - 128:
                herey = height - 128
        elif showHallway2:
            if self.x > width - 90:#right
                herex = width - 90
            elif self.x < -LEFT_OF_PLAYER:#left
                herex = width - 100 - 32
                showHallway1 = True
                showHallway2 = False
            if self.y < 120:
               herey = 120
            if self.y > height - 128:
                herey = height - 128
            
        #bedroom bounds
        if showBedroom:
            desk_rect = pygame.Rect(85,180-TOP_OF_PLAYER,215-LEFT_OF_PLAYER,100)#desk
            bed_rect = pygame.Rect(0-LEFT_OF_PLAYER,180-TOP_OF_PLAYER,120,180)
            bedDoor_rect = pygame.Rect(320-LEFT_OF_PLAYER,90,150,180)#SUBTRACT BC LEFT#SUBTRACT 90 BC UP
                    
            if desk_rect.collidepoint(herex, herey): 
                return #dont move at all (dont run 'move' anymore once)
            elif bed_rect.collidepoint(herex,herey):#top right
                return

            if bedDoor_rect.collidepoint(herex,herey):# top left
                showE = True
                bedDoor = True
            else:
                showE=False
            self.x = herex
            self.y = herey
            #MAKE SURE SPAWN BY DOOR
            if bedDoor and showHallway1:
                self.x = 360
                self.y = 310
                showBedroom = False
                showE = False
                bedDoor = False
            #hallway bounds
        elif showHallway1:
            drawer_rect = pygame.Rect(270+LEFT_OF_PLAYER,180-TOP_OF_PLAYER,180,120)
            bedEntrance_rect = pygame.Rect(380,310,140,250)
            if drawer_rect.collidepoint(herex+128,herey):
                return
            if bedEntrance_rect.collidepoint(herex + 128, herey+128):
                showE = True
                hallwayBed = True
            else:
                showE = False
            self.x = herex
            self.y = herey
        elif showHallway2: #make me my own method
            houseDoor_rect = pygame.Rect(0,0,0,0)
            kitchenEntrance_rect = pygame.Rect(400,0,150,220)
            drawer2_rect = pygame.Rect(135+LEFT_OF_PLAYER,180-TOP_OF_PLAYER,180,120)
            if drawer2_rect.collidepoint(herex+128,herey):
                return
            if houseDoor_rect.collidepoint(herex+128, herey):
               showE = True
               hallwayOutside = True
            elif kitchenEntrance_rect.collidepoint(herex +128,herey):
                showE = True
                hallwayKitchen = True
            else:
                showE = False

            self.x = herex
            self.y = herey
        #kitchen bounds
        elif showKitchen:
            table_rect = pygame.Rect(65 - LEFT_OF_PLAYER,325,210,170)
            chair_rect = pygame.Rect(0 - LEFT_OF_PLAYER,370,90,170)
            counter_rect = pygame.Rect(0,0,0,0)
            kitchenDoor_rect = pygame.Rect(330 + LEFT_OF_PLAYER,230,280,250)
            if table_rect.collidepoint(herex,herey + 128):
                return
            if chair_rect.collidepoint(herex, herey + 128):
                return

            if kitchenDoor_rect.collidepoint(herex+128, herey):
                kitchenDoor = True
                showE = True
            else:
                showE = False

            self.x = herex
            self.y = herey

        #flip if going left
        if px < 0:
            self.direction = "left"
        elif px > 0:
            self.direction = "right"
#Player
player = Player(256,256)

class Door():
    doorIMAGE = pygame.image.load('Door.PNG')
    doorIMAGE = pygame.transform.scale(doorIMAGE, (256,256))

    def __init__(self):
        super().__init__()
        self.opacity = 100
        self.fadeSpeed = 5
    def CREATEdoorPos(self):
        """returns door position depending on the room"""
        global showHallway1, showHallway2, showKitchen
        doorPos = (330,282)
        if showHallway1 or showKitchen:
            doorPos = (250,282)
        elif showHallway2:
            doorPos = (0,282)
        else:
            doorPos = (-1000,-1000)
        return doorPos
    def setOpacity(self,player):
        """sets opacity of the door when player collides with it"""
        doorPos = self.CREATEdoorPos()
        #opaque door alpha value is 255 
        rect= pygame.Rect(doorPos[0] + 40,doorPos[1] - 20,216,256)
        if rect.collidepoint(player.x+80,player.y): #rect is a parameter
            self.opacity = max(100,self.opacity - self.fadeSpeed)
        else:
            self.opacity = min(200,self.opacity +self.fadeSpeed)
        self.doorIMAGE.set_alpha(self.opacity)# when player touches this door, it decreases opacity
    def draw(self,screen):

        doorPos = self.CREATEdoorPos()
        screen.blit(self.doorIMAGE,(doorPos))

door = Door()


    
#this is the main loop
while running: 
    mouse = pygame.mouse.get_pos()
    now = pygame.time.get_ticks()
    #this is the event loop, BUTTONS TO BE PRESSED ONCE go here
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and showSpace == True and now - lastPressed > 1000:
                lastPressed = now
                if showthumbnail == True:
                    showthumbnail = False
                    showSpace = False
                    showHELP = True
                    player.x, player.y = 256 - 64,400 - 64
                elif showHELP == True and not showthumbnail:
                    showSpace = False
                    showBedroom = True
                    showHELP = False
            elif event.key == pygame.K_e and showE == True:
                print("E has been pressed")
                showBlack = True
                blackStart = pygame.time.get_ticks()
                if bedDoor and showBedroom:
                    player.x,player.y = 360,310
                    showHallway1 = True
                    showBedroom = False
                    bedDoor = False # put the room name transition code here
                elif hallwayBed and showHallway1:
                    player.x,player.y = 360,150
                    showBedroom = True
                    showHallway1 = False
                    hallwayBed = False
                elif hallwayKitchen and showHallway2:
                    player.x,player.y = 384,300
                    showKitchen = True
                    showHallway2 = False
                    hallwayKitchen = False
                elif kitchenDoor and showKitchen:
                    player.x,player.y = 390,290
                    showHallway2 = True
                    showKitchen = False
                    kitchenDoor = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse)

    if showBlack and blackStart is not None: #better time and None is every type of 0
        if now - blackStart >= 5000:
            showBlack = False
            blackStart = None
        
    #MOOOOOOOOOOOOOVING
    #baha no move here

    #this how make buttons holdable
    if not showBlack:        
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
            player.is_moving = True
        else:
            player.is_moving = False
  
        if keys[pygame.K_w]:
                player.move(0,-2)#move rules only work because you use in main loop
        if keys[pygame.K_s]:
            player.move(0,2)
        if keys[pygame.K_a]:
                player.move(-2,0)
        if keys[pygame.K_d]:
                player.move(2,0)

    #mark
        screen.fill(bgcolour) 
        if showthumbnail:
            screen.blit(thumbnail, (0,0))

        if showHELP == True:
            showSpace = True
            screen.blit(helpscreen, (0,0))
    ##ORDER OF APPEARANCE MATTERS WHAT IS SAID FIRST IS BEHIND
        #rooms

        if showBedroom == True:
            screen.blit(bedroom, (0,0))
        if showHallway1:
            screen.blit(hallway1,(0,0))
        if showHallway2:
            screen.blit(hallway2,(0,0))
        if showKitchen:
            screen.blit(kitchen, (0,0))
            
        #buttons
        if showSpace:
            screen.blit(space, space_rect)

        if showE == True:
            screen.blit(E,(0,height - 64))

        #CHARACTER STUFF
        if showHELP == False and showthumbnail == False:
            player.update()
            player.draw(screen)
            
        #DOOOOOOR STUFF????
        door.setOpacity(player)
        door.draw(screen)
    #if i put black here will it pritn over player and door??
    else:
        black = pygame.Surface((512,512))
        black.fill((0,0,0))
        screen.blit(black,(0,0))
        showE = False
        showSpace = False
    #should stay at bottom
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()
