import pygame
import time
import random

pygame.init()

white = (255, 255, 255) #define colours
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800 #window dimensions
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))  # surface object

pygame.display.set_caption('Slytherin') #icon and title
icon = pygame.image.load("apple2.png")
pygame.display.set_icon(icon)  

img = pygame.image.load("snake2.png") #snakehead
apple = pygame.image.load("apple2.png")  #apple

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 10
darkMode = False

direction = "Right"  #initial


smallfont = pygame.font.SysFont("comicsansms", 25) #font sizes
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 75)


def pause(scored): #pause screen
    paused=True
    message_to_screen("Paused",
                          black,
                          -100,
                          size="large")

    message_to_screen("Press C to continue or Q to quit Quit",
                      black,
                      25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    paused = False
    else:
        for timer in range(3):
            message_to_screen(str(3-timer),red,0+timer*100,"large")
            pygame.display.update()
            time.sleep(1)
        
        clock.tick(4)

def score(scored): #display score
    text = smallfont.render("Score: " + str(scored), True, black)
    gameDisplay.blit(text, [0, 0])


def randAppleGen(): #random apple location generator
    randAppleX = random.randrange(0, display_width - AppleThickness)
    randAppleY = random.randrange(0, display_height - AppleThickness)
    return randAppleX, randAppleY


def game_intro(): #intro screen
    global white
    global black
    global darkMode
    global apple
    global img
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    intro = False
                    gameLoop()
                elif event.key == pygame.K_d:
                    if darkMode == False:
                        darkMode = True
                        white, black = black, white
                        img = pygame.image.load("snake3.png")
                        apple = pygame.image.load("apple3.png")
                    else:
                        darkMode = False
                        white, black = black, white
                        img = pygame.image.load("snake2.png")
                        apple = pygame.image.load("apple2.png")
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slytherin",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the screen is to eat red apples",
                          black,
                          -30)
        message_to_screen("The more apples you eat ,the longer you get",
                          black,
                          10)
        message_to_screen("If you run into yourself or the walls you die",
                          black,
                          50)
        message_to_screen("Press C to play , P to pause or Q to quit",
                          black,
                          180)
        message_to_screen("Press D to toggle dark mode on/off",
                          black,
                          220)
        pygame.display.update()
        clock.tick(4)


def snake(block_size, snakeList): #snake
    head = img
    if direction == "Right": #rotate snake head acc to direction
        head = pygame.transform.rotate(img, 270)
    elif direction == "Left":
        head = pygame.transform.rotate(img, 90)
    elif direction == "Up":
        head = img
    elif direction == "Down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1])) #blit snake head

    for XnY in snakeList[:-1]: #draw snake
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, colour, size):
    textSurface = smallfont.render(text, True, colour)
    if size == "small":
        textSurface = smallfont.render(text, True, colour)
    elif size == "medium":
        textSurface = medfont.render(text, True, colour)
    if size == "large":
        textSurface = largefont.render(text, True, colour)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, colour, y_displace=0, size="small",x_displace=0): #to diplay message
    textSurface, textRect = text_objects(msg, colour, size)
    textRect.center = (display_width / 2) + x_displace , (display_height / 2) + y_displace
    gameDisplay.blit(textSurface, textRect)


def gameLoop(): #gameloop
    global white
    global black
    global direction
    global apple
    global img
    global darkMode
    snakeList = [] #snake
    snakeLength = 1

    lead_x = display_width / 2 #initial pos of snake
    lead_y = display_height / 2

    lead_x_change = 10 
    lead_y_change = 0
    direction = "Right"

    gameExit = False
    gameOver = False

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:
        if gameOver:
            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                              size="large")

            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): #to handle events
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_y_change = 0
                    lead_x_change = -block_size
                    direction = "Left"
                elif event.key == pygame.K_RIGHT:
                    lead_y_change = 0
                    lead_x_change = +block_size
                    direction = "Right"
                elif event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                    direction = "Up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "Down"
                elif event.key==pygame.K_SPACE  or event.key==pygame.K_p:
                    pause(snakeLength - 1)
                elif event.key == pygame.K_d:
                    if darkMode == False:
                        darkMode = True
                        white, black = black, white
                        img = pygame.image.load("snake3.png")
                        apple = pygame.image.load("apple3.png")
                    else:
                        darkMode = False
                        white, black = black, white
                        img = pygame.image.load("snake2.png")
                        apple = pygame.image.load("apple2.png")
                        

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        gameDisplay.blit(apple, (randAppleX, randAppleY))
        
        snakeHead = [lead_x, lead_y]
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        if snakeHead in snakeList[:-1]:
            gameOver = True

        snake(block_size, snakeList)
        score(snakeLength - 1)
        pygame.display.update()

        if randAppleX < lead_x < randAppleX + AppleThickness or randAppleX < lead_x + block_size < randAppleX + AppleThickness:
            if randAppleY < lead_y < randAppleY + AppleThickness or randAppleY < lead_y + block_size < randAppleY + AppleThickness:
                snakeLength = snakeLength + 1
                randAppleX, randAppleY = randAppleGen()
                
        clock.tick(FPS)

    pygame.quit()
    quit()


game_intro()

