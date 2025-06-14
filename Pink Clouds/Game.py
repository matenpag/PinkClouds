import pygame
clock = pygame.time.Clock()
pygame.init()
#scren 
width = 512
height = width
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pink Clouds')
Icon = pygame.image.load("Lily.PNG")
pygame.display.set_icon(Icon)
#variables for background variables
text_font = pygame.font.Font("PixelifySans-Regular.ttf",24)
bgcolour = (115,170,250) 
running  = True 
pressed = False
lastPressed = 0
start_ticks = pygame.time.get_ticks()
interact = ""
interacted = ""
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
showHelpScreen = False
#DAYS AND CHOICES
day = 1
scene = 0 #the hundreds represent the scene the digits after 
play_scene = False
goal = ""
goal_display = text_font.render(goal, True, (255,255,255))
showGoal = False
goal_rect = goal_display.get_rect(topright = (width - 6, 6))

black_screen = pygame.Surface((512,512), pygame.SRCALPHA)
black_screen.fill((0,0,0,255))
day_font = pygame.font.Font("PixelifySans-Regular.ttf",36)
date = "Friday 6th Febuary 2026"

karma = 0
cut_flower = False
write_threat = False
#DIARYY PAGES
diary_font = pygame.font.Font("PixelifySans-Regular.ttf",20)
page1 = ""
showPage1 = False
#ROOMS
roomName = ""
fadeRoomName = False
roomName_opacity = 255
roomName_font = pygame.font.Font("Lexend-SemiBold.ttf",width//8)
roomName_display = roomName_font.render(roomName, True, (255,255,255)).convert_alpha()#NEED THIS FOR NON IMAGES
roomName_rect = roomName_display.get_rect(center = (width//2,height//2))
showRoomName = False

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
arrow_y = 32
button = pygame.image.load("Button.png")
button = pygame.transform.scale(button, (24,24))
showButton = False
button_rect = button.get_rect()
button_down = pygame.image.load("Button Down.png")
button_down = pygame.transform.scale(button_down, (24,24))
showButton_down = False

space = pygame.image.load("Space.png")
space = pygame.transform.scale(space, (128,128))
space_rect = space.get_rect(center = (width - 64, height - 32))
showSpace = True

E = pygame.image.load("E.png")
E = pygame.transform.scale(E, (64,64))
E_rectangle = E.get_rect()
showE = False

Y = pygame.image.load("Y.png")
Y = pygame.transform.scale(Y, (32,32))
showY = False
Y_down = pygame.image.load("Y Down.png")
Y_down = pygame.transform.scale(Y_down, (32,32))
showY_down = False
Y_rect = pygame.Rect(400,474,32,32)

N = pygame.image.load("N.png")
N = pygame.transform.scale(N, (32,32))
showN = False
N_down = pygame.image.load("N Down.png")
N_down = pygame.transform.scale(N_down, (32,32))
showN_down = False
N_rect = pygame.Rect(436,474,32,32)

MENU = pygame.image.load("Menu.PNG")
MENU = pygame.transform.scale(MENU, (96,96))
MENU_down = pygame.image.load("Menu Down.PNG")
MENU_down = pygame.transform.scale(MENU_down, (96,96))
MENU_rect = pygame.rect.Rect(1,1,96,28)
MENU_down_RECT = pygame.rect.Rect(1,1,96,28)
showMENU = False
showMENU_down = False

BAG = pygame.image.load("Bag.PNG")
BAG = pygame.transform.scale(BAG, (96,96))
BAG_rect = pygame.rect.Rect(1,30,96,28)
BAG_down = pygame.image.load("Bag Down.PNG")
BAG_down = pygame.transform.scale(BAG_down, (96,96))
BAG_down_rect = pygame.rect.Rect(1,30,96,28)
showBAG = False
showBAG_down = False
inventory_back = pygame.Surface((128,512)) #0,0
inventory_back.fill((0,0,0))
showInventory = False
inventory = ["a","phone"]
inventory_text = ""
inventory_text_display = text_font.render(inventory_text, True,(255,255,255))
inventory_text_y = 64
arrow = pygame.image.load("Arrow.png")
arrow = pygame.transform.scale(arrow, (32,32))
arrow_pos = 0


HELP = pygame.image.load("Help.png")
HELP = pygame.transform.scale(HELP, (96,96))
HELP_rect = pygame.rect.Rect(1,59, 96,28)
HELP_down = pygame.image.load("Help Down.PNG")
HELP_down = pygame.transform.scale(HELP_down, (96,96))
showHELP = False
showHELP_down = False

EXIT = pygame.image.load("Exit.PNG")
EXIT = pygame.transform.scale(EXIT,(96,96))
EXIT_rect = pygame.rect.Rect(1,1,96,28)
EXIT_down = pygame.image.load("Exit Down.PNG")
EXIT_down = pygame.transform.scale(EXIT_down,(96,96))
showEXIT = False
showEXIT_down = False
#misc
diary = pygame.image.load("Diary.PNG")
diary = pygame.transform.scale(diary, (128,128))
diary = pygame.transform.flip(diary, True,False)
showDiary = True
BOOK = pygame.image.load("BOOK.PNG")
BOOK = pygame.transform.scale(BOOK, (512,512))
showBOOK = False

knife = pygame.image.load("knife.png")
knife = pygame.transform.scale(knife, (64,64))
showKnife = False
knife_inventory = "knife"
showKnife_inventory = False

dinner1 = pygame.image.load("Chicken Dinner.png")
dinner1 = pygame.transform.scale(dinner1, (32,32))
showDinner1 = False

phone = pygame.image.load("Phone.png")
phone = pygame.transform.scale(phone,(512,512))
showPhone = False
call = pygame.image.load("Call.png")
call = pygame.transform.scale(call, (64,64))
call_down = pygame.image.load("Call Down.png")
call_down = pygame.transform.scale(call_down, (64,64))
call_rect = pygame.Rect(285,50,64,64)
message = pygame.image.load("Message.png")
message = pygame.transform.scale(message, (64,64))
message_down = pygame.image.load("Message Down.png")
message_down = pygame.transform.scale(message_down, (64,64))
message_rect = pygame.Rect(210,50,64,64)
notification = pygame.image.load("Notification.png")
notification = pygame.transform.scale(notification, (16,16))
showNotification = False

#dialogue
text_full = ""
text = ""
text_display = text_font.render(text,True,(255,255,255))
text_rect = text_display.get_rect(topleft = (6,400))
text_count = 0
text_timer = 0
text_speed = 40
text_y = 400
line1 = ""
line2 = ""
line3 = ""

showConfirmation = False

description = pygame.Surface((504,108), pygame.SRCALPHA) #4,400 x,y
description.fill((55,55,55,127))
showDescription = False

pink_box = pygame.Surface((504,108), pygame.SRCALPHA)
pink_box.fill((255,0,255,170))

box = ""


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
        '''allow player to move and establish boundaries'''
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
            if self.y > height - 132:#down
                herey = height - 132
        elif showHallway1:
            if self.x < -LEFT_OF_PLAYER:#left
                herex = -LEFT_OF_PLAYER
            elif self.x > width - 90:#right
                herex = 32 - LEFT_OF_PLAYER
                showHallway2 = True #make variable for all rooms
                showHallway1 = False
            if self.y < 120:
               herey = 120
            if self.y > height - 132:
                herey = height - 132
        elif showHallway2:
            if self.x > width - 90:#right
                herex = width - 90
            elif self.x < -LEFT_OF_PLAYER:#left
                herex = width - 100 - 32
                showHallway1 = True
                showHallway2 = False
            if self.y < 120:
               herey = 120
            if self.y > height - 132:
                herey = height - 132
            
        #bedroom bounds
        if showBedroom:
            desk_rect = pygame.Rect(85,180-TOP_OF_PLAYER,215-LEFT_OF_PLAYER,100)#desk
            bed_rect = pygame.Rect(0-LEFT_OF_PLAYER,180-TOP_OF_PLAYER,120,180)
            bedDoor_rect = pygame.Rect(320-LEFT_OF_PLAYER,90,150,180)#SUBTRACT BC LEFT#SUBTRACT 90 BC UP
            plant_rect = pygame.rect.Rect(450 + LEFT_OF_PLAYER,440,200,200)        
            if desk_rect.collidepoint(herex, herey): 
                return #dont move at all (dont run 'move' anymore once)
            elif bed_rect.collidepoint(herex,herey):#top right
                return
            elif plant_rect.collidepoint(herex + 128, herey +128):
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
            table_rect = pygame.Rect(60 - LEFT_OF_PLAYER,335,210,170)
            chair_rect = pygame.Rect(0 - LEFT_OF_PLAYER,370,90,170)
            counter_rect = pygame.Rect(-200,200-TOP_OF_PLAYER,712,60)
            kitchenDoor_rect = pygame.Rect(330 + LEFT_OF_PLAYER,230,280,250)
            if table_rect.collidepoint(herex,herey + 128):
                return
            elif chair_rect.collidepoint(herex, herey + 128):
                return
            elif counter_rect.collidepoint(herex,herey):
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
class Mum(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.current = 0
        self.animationSpeed = 0.2
        self.is_moving = False
        self.frames = []
        self.frames_back= []
        self.load_frames()
        self.animation = "idle"

    def load_frames(self):
        idle_frame_names = ["Mum Stand 01.PNG","Mum Stand 01.PNG", "Mum Stand 02.PNG", "Mum Stand 03.PNG",
                            "Mum Stand 04.PNG", "Mum Stand 05.PNG", "Mum Stand 06.PNG",
                            "Mum Stand 07.PNG", "Mum Stand 08.PNG",]
        
        back_frame_names = ["Mum Back 01.PNG","Mum Back 01.PNG", "Mum Back 02.PNG", "Mum Back 03.PNG",
                            "Mum Back 04.PNG", "Mum Back 05.PNG", "Mum Back 06.PNG",
                            "Mum Back 07.PNG", "Mum Back 08.PNG",]
        for frame_name in idle_frame_names:
            frame = pygame.image.load(frame_name)
            frame = pygame.transform.scale(frame, (160,160))
            self.frames.append(frame)

        for frame_name in back_frame_names:
            frame = pygame.image.load(frame_name)
            frame = pygame.transform.scale(frame, (160,160))
            self.frames_back.append(frame)
    def update(self):
        if self.animation == "idle":
            self.current += self.animationSpeed
            if self.current >= len(self.frames):
                self.current = 0
        elif self.animation == "back":
            self.current += self.animationSpeed
            if self.current >= len(self.frames_back):
                self.current = 0
                    
    def draw(self,screen):
        if self.animation == "back":
                current_frame = self.frames_back[int(self.current)]
        else:
            current_frame = self.frames[int(self.current)]
        screen.blit(current_frame, (self.x, self.y))
            
mum = Mum(256,256)
        
class Door():
    doorIMAGE = pygame.image.load('Door.PNG')
    doorIMAGE = pygame.transform.scale(doorIMAGE, (256,256))

    def __init__(self):
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

class Dot():
    def __init__(self):
        self.current = 0
        self.animationSpeed = 0.05
        self.frames =  []
        self.show = False
        self.loadFrames()
    def loadFrames(self):
        frameNames = ["Dot 0.png", "Dot 1.png", "Dot 2.png", "Dot 3.png",
                  "Dot 4.png", "Dot 5.png"]
        for frames in frameNames:
            frame = pygame.image.load(frames)
            frame = pygame.transform.scale(frame, (32,32))
            self.frames.append(frame)
    def update(self):
        '''update animation'''
        self.current += self.animationSpeed
        if self.current > len(self.frames):
            self.current = 0
    def interact(self):
        '''shows when hovering over an interactable item'''
        global mouse, showBedroom, showHallway1, showHallway2, showKitchen, interact
        global showBOOK, showKnife, showDinner1
        if not showBOOK:
            if showBedroom:
                plant_rect = pygame.rect.Rect(435,430,512-436,512-431)
                diary_rect = pygame.rect.Rect(160,190,80,50)
                if plant_rect.collidepoint(mouse):
                    self.show = True
                    interact = "plant pot"
                elif diary_rect.collidepoint(mouse):
                    self.show = True
                    interact = "diary"
                else:
                    self.show = False
                    interact = ""
            elif showHallway1:
                painting_rect = pygame.rect.Rect(256,70,144,70)
                if painting_rect.collidepoint(mouse):
                    self.show = True
                    interact = "painting_1"
                else:
                    self.show = False
                    interact = ""
            elif showHallway2:
                painting_rect = pygame.rect.Rect(120,70,144,70)
                if painting_rect.collidepoint(mouse):
                    self.show = True
                    interact = "painting_2"
                else:
                    self.show = False
                    interact = ""
            elif showKitchen:
                fridgeNote_rect = pygame.rect.Rect(40,170,55,50)
                knife_rect = pygame.rect.Rect(315,180,30,30)
                dinner1_rect = pygame.rect.Rect(125,400,32,32)
                if fridgeNote_rect.collidepoint(mouse):
                    self.show = True
                    interact = "fridge note"
                elif knife_rect.collidepoint(mouse) and showKnife:
                    self.show = True
                    interact = "knife"
                elif dinner1_rect.collidepoint(mouse) and showDinner1:
                    self.show = True
                    interact = "dinner 1"
                else:
                    self.show = False
                    interact = ""
            else:
                self.show = False
                interact = ""
        else:
            self.show = False
        
    def draw(self,screen,mouse):
        if self.show:
            current_frame = self.frames[int(self.current)]
            screen.blit(current_frame, (mouse[0]-32,mouse[1]-24))

dot = Dot()

def resetText():
    global text,text_count,text_y,current_line, line1,line2,line3, showDescription
    text = ""
    text_count = 0
    text_y = 400
    current_line = 0
    line1 = ""
    line2 = ""
    line3 = ""
    showDescription = True

def loadAllMisc():
    global showKnife, showDinner1
    showKnife = True
    showDinner1 = True


def wrapDiary(text,text_font,colour,pos,max_width,screen):
    words = text.split(" ")
    x,y = pos
    space = text_font.size(" ")[0]
    line = ""

    for word in words:
        word_surface = text_font.render(word,True,colour)
        word_width = word_surface.get_width()

        if text_font.size(line + word)[0] > max_width:
            line_display = text_font.render(line,True,colour)
            screen.blit(line_display, (x,y))
            y += text_font.get_height() + 4
            line = word + " "
        else:
            line += word + " "

    if line:
        line_surface = text_font.render(line, True, colour)
        screen.blit(line_surface, (x, y))

def nextDay(text, font, background):
    global play_scene, scene, bedroom, player
    play_scene = False
    opacity = 255
    date_display = font.render(text, True, (255, 255, 255)).convert_alpha()
    date_rect = date_display.get_rect(center=(256, 256))
    fade_speed = 1 
    player.update()
    player.draw(screen)
        
    while opacity >= 0:
        screen.blit(bedroom,(0,0))
        player.x,player.y = 128, 256
        # Clear screen first

        # Fade background
        background.fill((0, 0, 0, opacity))
        screen.blit(background, (0, 0))

        # Fade text
        faded_text = date_display.copy()
        faded_text.set_alpha(opacity)
        screen.blit(faded_text, date_rect)

        pygame.display.flip()
        pygame.time.delay(20)
        fade_speed += 0.2
        opacity -= fade_speed
        
    play_scene = True
    scene += 1
    print(play_scene, scene)
                           
#this is the main loop
while running: 
    mouse = pygame.mouse.get_pos()
    now = pygame.time.get_ticks()
    #this is the event loop, BUTTONS TO BE PRESSED ONCE go here
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        elif event.type == pygame.KEYDOWN:
            #lastPressed = now
            if event.key == pygame.K_SPACE and showSpace == True:
                showSpace = False
                showPhone = False
                if play_scene:
                    scene += 1
                    print(scene)
                if showthumbnail == True:
                    showthumbnail = False
                    showSpace = False
                    showHelpScreen = True
                    showMENU_down = False
                    player.x, player.y = 256 - 64,400 - 64
                elif showHelpScreen == True and not showthumbnail and now - lastPressed > 1000:
                    showSpace = False
                    showBedroom = True
                    showHelpScreen = False
                    showMENU = True
                    showRoomName = True
                    loadAllMisc()
                    play_scene = True
                if showDescription:
                    showDescription = False
                    showSpace = False
                    interacted = ""
                    text_full = ""
                if interacted == "diary":
                    showBOOK = False
                    showSpace = False
                    if scene == 7:
                        scene = 8
                        play_scene = True
                    interacted = ""
                if interacted == "phone":
                    showSpace = False
                    showPhone = False
                    interacted = ""
            elif event.key == pygame.K_y:
                if interacted == "knife":
                    showKnife = False
                    showDescription = False
                    interacted = ""
                    showConfirmation = False
                elif interacted == "dinner 1":
                    showDinner1 = False
                    showDescription = False
                    interacted = ""
                    showConfirmation = False
                    showGoal = False
                    play_scene = True
                    scene = 4
            elif event.key == pygame.K_n:
                interacted = ""
                showDescription = False
                showConfirmation = False
            elif event.key == pygame.K_e and showE == True:
                print("E has been pressed")
                if bedDoor and showBedroom:
                    player.x,player.y = 360,310
                    roomName = "HALLWAY"
                    showRoomName = True
                    showHallway1 = True
                    showBedroom = False
                    bedDoor = False # put the room name transition code here
                elif hallwayBed and showHallway1:
                    player.x,player.y = 360,150
                    roomName = "BEDROOM"
                    showRoomName = True
                    showBedroom = True
                    showHallway1 = False
                    hallwayBed = False
                elif hallwayKitchen and showHallway2:
                    player.x,player.y = 320,350
                    roomName = "KITCHEN"
                    showBedroom = False
                    showRoomName = True
                    showKitchen = True
                    showHallway2 = False
                    hallwayKitchen = False
                elif kitchenDoor and showKitchen:
                    player.x,player.y = 340,120 #390,290 to enter house
                    roomName = "HALLWAY"
                    showRoomName = True
                    showHallway2 = True
                    showKitchen = False
                    kitchenDoor = False
            elif event.key == pygame.K_UP:
                if not arrow_y - text_font.get_height() + 4 < 32:
                    arrow_y -= text_font.get_height() + 4
                    arrow_pos -= 1
            elif event.key == pygame.K_DOWN:
                if not arrow_y + text_font.get_height() + 4  > (len(inventory)*(text_font.get_height() + 4)) + 28 - text_font.get_height():
                    arrow_y += text_font.get_height() + 4
                    arrow_pos += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse)
            if showMENU_down:
                MENU_rect = pygame.rect.Rect(1,1,96,116)
                MENU_down_RECT = pygame.rect.Rect(1,1,96,28)
                showBAG = True
                showHELP = True
            if showHELP_down:
                showHelpScreen = True
            if showBAG_down:
                showInventory = True
            if showEXIT_down:
                showInventory = False
                showEXIT = False
                showEXIT_down = False
                showButton = False
                showButton_down = False
            if interact == "plant pot":
                box = "grey"
                text_full = "An oriental lily, obviously you can't tell. " #have to put space after i think
                resetText()
                interacted = "plant pot"
            elif interact == "diary" and not play_scene:
                showBOOK = True
                interacted = "diary"
                if scene == 7:
                    showGoal = False
            elif interact == "painting_1":
                box = "grey"
                text_full = "A picture of the mountains we went to. "
                resetText()
                interacted = "painting_1"
            elif interact == "painting_2":
                box = "grey"
                text_full = "An old painting I made in primary school. I|wish Mum would take it down."
                resetText()  
                interacted = "painting_2"
            elif interact == "fridge note":
                box = "grey"
                text_full = "A heartfelt letter from someone. The|sender's name is blocked out."
                resetText()  
                interacted = "fridge note"
            elif interact == "knife":
                box = "grey"
                text_full = "A kitchen knife. Nothing more to it. Put the |knife in bag?"
                resetText()  
                interacted = "knife"
                showConfirmation = True
                showSpace = False
            elif interact == "dinner 1":
                box = "grey"
                text_full = "Some nice chicken for your dinner. Eat|dinner?"
                resetText()  
                interacted = "dinner 1"
                showConfirmation = True
                showSpace = False
            elif Y_rect.collidepoint(mouse):
                if interacted == "knife":
                    showKnife = False
                    showDescription = False
                    interacted = ""
                    showConfirmation = False
                elif interacted == "dinner 1":
                    showDinner1 = False
                    showDescription = False
                    interacted = ""
                    showConfirmation = False
                    showGoal = False
                    play_scene = True
                    scene = 4
            elif N_rect.collidepoint(mouse):
                    interacted = ""
                    showDescription = False
                    showConfirmation = False
            elif button_rect.collidepoint(mouse):
                interact = inventory[arrow_pos] + "_inv"
                                    
    if MENU_rect.collidepoint(mouse) and not showthumbnail and not showHelpScreen: #event.pos get position of event (mouse)
        showMENU_down = True
    else:
        showMENU_down = False
        showBAG = False
        showBAG_down = False
        showHELP = False
        showHELP_down = False
        MENU_rect = pygame.rect.Rect(1,1,96,28)
        MENU_down_RECT = pygame.rect.Rect(1,1,96,28)
        
    if BAG_rect.collidepoint(mouse) and showBAG:
        showBAG_down = True
    else:
        showBAG_down = False

    if HELP_rect.collidepoint(mouse) and showHELP:
        showHELP_down = True
    else:
        showHELP_down = False

    if EXIT_rect.collidepoint(mouse) and showEXIT:
        showEXIT_down = True
    else:
        showEXIT_down = False

    if Y_rect.collidepoint(mouse) and showY:
        showY_down = True
    else:
        showY_down = False

    if N_rect.collidepoint(mouse) and showN:
        showN_down = True
    else:
        showN_down = False

    if button_rect.collidepoint(mouse) and showButton:
        showButton_down = True
    else:
        showButton_down = False
    
    if showInventory:
        if interact == "knife_inv":
            box = "grey"
            text_full = "A kitchen knife. Nothing more to it."
            resetText()  
            showSpace = True
            interacted = "knife"
        elif interact == "phone_inv": 
            showSpace = True
            showPhone = True
            interacted = "phone"

#MOOOOOOOOOOOOOVING
#baha no move here
#thats a lie therr is moving here

###THIS IS FOR DISPLAY THINGS ONLYYYYYY
#this how make buttons holdable
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
##ORDER OF APPEARANCE MATTERS WHAT IS SAID FIRST IS BEHIND
    #rooms

    if showBedroom == True:
        screen.blit(bedroom, (0,0))
        if showDiary:
            screen.blit(diary, (132,150))
    if showHallway1:
        screen.blit(hallway1,(0,0))
    if showHallway2:
        screen.blit(hallway2,(0,0))
    if showKitchen:
        screen.blit(kitchen, (0,0))
        if showKnife:
            showKnife_inventory = False
            screen.blit(knife, (300,168))
        else:
            showKnife_inventory = True

        if showDinner1:
            screen.blit(dinner1, (125,400))

    #adding items to inventory
    if showKnife_inventory:
        showKnife = False
        if "knife" not in inventory:
            inventory.append(knife_inventory)
    
    #CHARACTER STUFF????
    if showHelpScreen == False and showthumbnail == False:
        #MOTHERRR
        if scene in [14,15,16,17,18,19] and showKitchen:
            mum.animation = "back"
            mum.x, mum.y = 275,140
            mum.update()
            mum.draw(screen)
        player.update()
        player.draw(screen)
        
    #buttons and description
    if showE:
        screen.blit(E,(0,height - 64))

    #DOOOOOOR STUFF????
    door.setOpacity(player)
    door.draw(screen)


    ####
    if showHELP:
        screen.blit(HELP, (0,32))

    if showHELP_down:
        screen.blit(HELP_down, (0,32))
        
    #inventory

    
    if showBAG:
        screen.blit(BAG, (0,0))
    if showBAG_down:
        screen.blit(BAG_down, (0,0))
    if showInventory:
        button_rect = pygame.Rect(132,arrow_y + 4,32,32)
        screen.blit(inventory_back,(0,0))
        inventory_text_y = 32
        showEXIT = True
        if arrow_y > (len(inventory)*(text_font.get_height() + 4)) + 28 - text_font.get_height():
            arrow_y -= text_font.get_height() + 4
        showButton = True
        #max_spaces_y = (len(inventory)+4)*len(inventory)*2
        for item in inventory:
            inventory_text_display = text_font.render(item,True,(255,255,255))
            screen.blit(inventory_text_display,(0,inventory_text_y))
            inventory_text_y += text_font.get_height() + 4
        screen.blit(arrow, (96,arrow_y))


    if showPhone and showInventory:
        showSpace = True
        showDescription = False
        dot.show = False
        screen.blit(phone, (65,0))
        screen.blit(message, (210,50))
        screen.blit(call, (285,50))
        if message_rect.collidepoint(mouse):
            screen.blit(message_down, (210,50))
        if call_rect.collidepoint(mouse):
            screen.blit(call_down, (285,50))
        
    if showDescription: #REMEMBER AS LONG AS THIS IS TRUE IT STAYS LIEK THIS
        showSpace = True
        if box == "grey":
            screen.blit(description, (4,400))
        elif box == "pink":
            screen.blit(pink_box,(4,400))
            
        lines = text_full.split("|")
        line1 = lines[0] if len(lines) >= 1 else ""
        line2 = lines[1] if len(lines) >= 2 else ""
        line3 = lines[2] if len(lines) >= 3 else ""

        # Always blit finished lines
        if current_line >= 1:
            screen.blit(text_font.render(line1, True, (255, 255, 255)), (text_rect[0], text_y))
        if current_line >= 2:
            screen.blit(text_font.render(line2, True, (255, 255, 255)), (text_rect[0], text_y + text_font.get_height() + 4))

        if current_line == 0:
            line = line1
        elif current_line == 1:
            line = line2
        elif current_line == 2:
            line = line3
        else:
            line = ""
            
        if text_count < len(line):
            if now - text_timer > text_speed:
                current_character = line[text_count]
                text_count += 1
                text = line[:text_count]
                text_display = text_font.render(text, True, (255, 255, 255))
                if current_character in [",", "."]:
                    text_timer = now + 200
                else:
                    text_timer = now
            y_offset = current_line * (text_font.get_height() + 4)
            screen.blit(text_display, (text_rect[0], text_y + y_offset))
        else:
            current_line += 1
            text_count = 0

    if showGoal:
        goal_display = text_font.render(("Task: "+goal), True, (255,125,200))
        goal_rect = goal_display.get_rect(topright = (width - 6, 6))
        screen.blit(goal_display,(goal_rect))
    if showY:
        screen.blit(Y, (400,474))
    if showY_down:
        screen.blit(Y_down, (400,474))

    if showN:
        screen.blit(N, (436,474))
    if showN_down:
        screen.blit(N_down, (436,474))        
    #... STUFF????
    dot.update()
    dot.interact()
    dot.draw(screen,mouse)

    if showConfirmation:
        showSpace = False
        showY = True
        showN = True
    else:
        showY = False
        showN = False

    if showButton:
        screen.blit(button, button_rect)
        
    if showButton_down:
        screen.blit(button_down, button_rect)
        
        
    if showBOOK:
        showSpace = True
        screen.blit(BOOK, (0,0,))
        if showPage1:
            page1 = "< Friday Feb 6th > I haven't been to Crawton High all week because of my fever. Apparently a new person joined. I can't wait to meet them!"
            page1Pos = (40,125)
            black = (0,0,0)
            wrapDiary(page1,diary_font,black,page1Pos,200,screen)
    if not showthumbnail and not showHelpScreen and not showBOOK:
        if play_scene:
            if scene == 0:
                box = "pink"
                text_full = "Even though I wasn't at school because of|my fever, it has been quite the week."
                resetText()
                showSpace = True
                scene = 1 #makes sure this ends and only does it once
            elif scene == 2:
                box = "pink"
                text_full = "Somehow it has made me very hungry, I|should go to the kitchen to get dinner."
                resetText()
                showSpace = True
                goal = "Get dinner"
                showGoal = True
                scene = 3
            elif scene == 4:
                box = "pink"
                text_full = "Food sure tastes better when you aren't|sick."
                resetText()
                showSpace = True
                scene = 5
            elif scene == 6:
                box = "pink"
                text_full = "The other thing I need to do is try to|fill in my diary."
                resetText()
                showSpace = True
                showPage1 = True
                goal = "Write diary entry"
                showGoal = True
                scene = 7
            elif scene == 8:
                box = "pink"
                text_full = "I've always wanted to have a full diary, I|should do this every night."
                resetText()
                showSpace = True
                scene = 9
            elif scene == 10:
                box = "pink"
                text_full = "It's easier to go to sleep feeling|acomplished."
                resetText()
                showSpace = True
                scene = 11
            elif scene == 12:
                day = 2
                date = "Saturday 7th February 2026"
                scene = 13
                nextDay("Saturday 7th February 2026",day_font,black_screen) #def nextDay(day,date,font,background):
            elif scene == 14:
                box = "grey"
                text_full = "*bzz*...*bzz*"
                resetText()
                showSpace = True
                scene = 15
            elif scene == 16:
                box = "pink"
                text_full = "nghh... What the-"
                resetText()
                showSpace = True
                scene = 17
                goal  = "Check phone"
                showGoal = True
                showNotification = True
            elif scene in [3,7,17]:
                play_scene = False

#menu buitl different
    if showMENU:
        screen.blit(MENU, (0,-32))
    if showMENU_down:
        screen.blit(MENU_down, (0,-32))
    
    if showHelpScreen == True:
        showSpace = True
        screen.blit(helpscreen, (0,0))
    if showSpace:
        screen.blit(space, space_rect)            
    if showEXIT:
        screen.blit(EXIT,(0,-32))
    if showEXIT_down:
        screen.blit(EXIT_down,(0,-32))
    if showNotification:
        if showInventory:
            if goal == "Check phone":
                screen.blit(notification, (75,((inventory.index("phone")+1.1)*text_font.get_height() + 12)))
        elif showBAG:
            screen.blit(notification, (84,49))
        else:
            screen.blit(notification, (84,20))
    #should stay at bottom
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()
