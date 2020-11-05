import pygame
pygame.init()

# Game Window
screnWidth = 1280
screenHeight = 720
gameWindow = pygame.display.set_mode((screnWidth, screenHeight))

# Game Title
pygame.display.set_caption("Gravity Runner")

# FPS
clock = pygame.time.Clock()
fps = 60

# Load Images
gameplayBgImg = pygame.image.load("Assets/GameplayBG.jpg")
groundImg1 = pygame.image.load("Assets/Ground.png")
groundImg2 = pygame.image.load("Assets/Ground.png")
groundImg2 = pygame.transform.rotate(groundImg2, 180)
playerImg = pygame.image.load("Assets/player/player1.png")
playerImg = pygame.transform.scale(playerImg, (75, 145)).convert_alpha()
rocketImg = pygame.image.load("Assets/Rocket.png")
rocketImg = pygame.transform.scale(rocketImg, (145, 50)).convert_alpha()
coinImg = pygame.image.load("Assets/Coin.png")

def text_screen(text,font_size, color, x, y):
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def Gameplaybackground():
    gameWindow.blit(gameplayBgImg, (0, 0))
    gameWindow.blit(groundImg1, (0, screenHeight-142))
    gameWindow.blit(groundImg2, (0, 0))

def player(x, y):
    gameWindow.blit(playerImg, (x, y))

def rocket(x, y):
    gameWindow.blit(rocketImg, (x, y))

def coin(x, y):
    gameWindow.blit(coinImg, (x, y))

def GameLoop():
    exit_game = False
    player_x = 40
    player_y = 442
    rocket_x = 600
    rocket_y = 200
    score_coin = 0
    coin_x = 300
    coin_y = 400

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()

        Gameplaybackground()
        player(player_x, player_y)
        rocket(rocket_x, rocket_y)
        coin(coin_x, coin_y)
        text_screen("coin: " + str(score_coin), 35, (255, 255, 255), 20, 20)
        pygame.display.update()
        clock.tick(fps)

def menu():
    pass

def gameover():
    pass
    
GameLoop()

                