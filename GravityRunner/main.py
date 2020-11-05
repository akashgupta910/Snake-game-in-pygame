import pygame
pygame.init()

# Game Window
screenWidth = 900
screenHeight = 600
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))

# Game Title 
pygame.display.set_caption("Gravity Runner")

# Fuction for Display text on screen
def text_screen(text, font_size, color, x, y):
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# Fuction of Menubar or Welcome

def Menu():
    # Menu Background
    menuImg = pygame.image.load("Assets/MenuBG.jpg")
    menuImg = pygame.transform.scale(menuImg, (screenWidth, screenHeight)).convert_alpha()

    # Play Button Image
    playImage = pygame.image.load("Assets/play.jpg")
    playImage = pygame.transform.scale(playImage, (200, 75)).convert_alpha()

    # Blit Image
    gameWindow.blit(menuImg, (0,0))
    gameWindow.blit(playImage, (340, 200))

    # Text Screen
    text_screen("Gravity Runner", 78, (255, 255, 255), 250, 50)

    # Display Update
    pygame.display.update()

    # Variable
    start_game = False

    # Loop for handling events
    while not start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True
                    Gameloop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_game = True
                Gameloop()
    
# Fuction of Main GameLoop

def Gameloop():

    # Variables
    init_velocity = 1
    velocity_x = 0
    player_x = 50
    player_y = 427
    exit_game = False

    # Game Background Image
    bgImg = pygame.image.load("Assets/GamePlayBG.jpg")
    bgImg = pygame.transform.scale(bgImg, (screenWidth, screenHeight)).convert_alpha()

    # First Ground Image
    first_groundImage = pygame.image.load("Assets/Ground.png")
    first_groundImage = pygame.transform.scale(first_groundImage, (screenWidth, 60)).convert_alpha()

    # Rocket Image
    rocketImg = pygame.image.load("Assets/Rocket.png")
    rocketImg = pygame.transform.scale(rocketImg, (100, 50)).convert_alpha()

    # Second Ground Image
    second_groundImage = pygame.image.load("Assets/Ground.png")
    second_groundImage = pygame.transform.scale(second_groundImage, (screenWidth, 60)).convert_alpha()
    second_groundImage = pygame.transform.rotate(second_groundImage, 180)

    # Player Image
    playerImg = pygame.image.load("Assets/player/Player1.png")
    playerImg = pygame.transform.scale(playerImg, (60, 120))

    playerImg = pygame.image.load("Assets/player/Player2.png")
    playerImg = pygame.transform.scale(playerImg, (60, 120))

    # Loop for Handling Events
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity 

                if event.key == pygame.K_LEFT:
                    velocity_x = - init_velocity

        # Blit Image
        import random
        rocket_speed = 6
        rocket_x = screenWidth-100
        # rocket_y = random.randint(100, 500)
        rocket_y = 200

        gameWindow.blit(bgImg, (0,0))
        gameWindow.blit(first_groundImage, (0, 538))
        gameWindow.blit(second_groundImage, (0, 7))
        gameWindow.blit(rocketImg, (rocket_x, rocket_y))
        gameWindow.blit(playerImg, (player_x, player_y))
        gameWindow.blit(playerImg, (player_x, player_y))

        rocket_x = -rocket_speed
        

        player_x += velocity_x

        # Display Update
        pygame.display.update()

Menu()
