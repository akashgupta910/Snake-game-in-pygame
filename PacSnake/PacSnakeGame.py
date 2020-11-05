import pygame
import random
pygame.init()

#Game Window
screenWidth = 900
screenHeight = 600
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))

#GameTitle
pygame.display.set_caption("PacSnake")

# BackgroundImage
bgImage = pygame.image.load("Images/background.jpg")
bgImage = pygame.transform.scale(bgImage, (screenWidth, screenHeight)).convert_alpha()

# Welcome Image
welImage = pygame.image.load("Images/welcome.jpg")
welImage = pygame.transform.scale(welImage, (screenWidth, screenHeight)).convert_alpha()

# SnakeImage
snkImage = pygame.image.load("Images/snake_right.png")
snkImage = pygame.transform.scale(snkImage, (50, 50)).convert_alpha()
# snkImage = pygame.transform.rotate(snkImage, 180)

#FoodImage
foodImage = pygame.image.load("Images/food.png")
foodImage = pygame.transform.scale(foodImage, (50, 50)).convert_alpha()

def text_screen(text, color, x, y):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, snk_list):
    for x,y in snk_list:
        gameWindow.blit(snkImage, (x, y))

# welcome
def welcome():
    exit_game = False
    black = (0,0,0)
    white = (255, 255, 255)

    wel_snkImage = pygame.image.load("Images/snake_right.png")
    wel_snkImage = pygame.transform.scale(wel_snkImage, (250, 250)).convert_alpha()

    gameWindow.blit(welImage, (0, 0))
    gameWindow.blit(wel_snkImage, (350, 90))
    text_screen("PacSnake", black, 380, 40)
    text_screen("Press SpaceBar to start the Game", black, 200, 370)
    pygame.display.update()

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

#GameLoop
def gameloop():

    #GameVariables
    exit_game = False
    snake_x = 50
    snake_y = 50
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screenWidth//2)
    food_y = random.randint(20, screenHeight//2)
    score = 0
    snk_list = []
    snk_length = 1
    black = (255, 255, 255)

    # FPS
    clock = pygame.time.Clock()
    fps = 60

    # SnakeImage
    snkImage = pygame.image.load("Images/snake_right.png")
    snkImage = pygame.transform.scale(snkImage, (50, 50)).convert_alpha()

    while not exit_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    velocity_y = init_velocity
                    velocity_x = 0
                    # snkImage = pygame.image.load("Images/snake_right.png")
                    # snkImage = pygame.transform.scale(snkImage, (50, 50)).convert_alpha()
                    # snkImage = pygame.transform.rotate(snkImage, 270)

                if event.key == pygame.K_UP:
                    velocity_y = - init_velocity
                    velocity_x = 0
                    # snkImage = pygame.image.load("Images/snake_right.png")
                    # snkImage = pygame.transform.scale(snkImage, (50, 50)).convert_alpha()
                    # snkImage = pygame.transform.rotate(snkImage, 90)

                if event.key == pygame.K_LEFT:
                    velocity_x = - init_velocity
                    velocity_y = 0
                    # snkImage = pygame.image.load("Images/snake_left.png")
                    # snkImage = pygame.transform.scale(snkImage, (50, 50)).convert_alpha()

                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity
                    velocity_y = 0
                    # snkImage = pygame.image.load("Images/snake_right.png")
                    # snkImage = pygame.transform.scale(snkImage, (50, 50)).convert_alpha()
                    # snkImage = pygame.transform.rotate(snkImage, 360)
                    
            
        if abs(snake_x - food_x)<30 and abs(snake_y-food_y)<30:
            score += 1
            snk_length += 5
            food_x = random.randint(20, screenWidth//2)
            food_y = random.randint(20, screenHeight//2)

        
        if snake_x == 0 or snake_x == screenWidth-45 or snake_y == 0 or snake_y == screenHeight-45:
            exit_game = True
            gameover()

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)>snk_length:
            del snk_list[0]

        if head in snk_list[:-1]:
            exit_game = True
            gameover()

        clock.tick(fps)

        gameWindow.blit(bgImage, (0,0))
        gameWindow.blit(foodImage, (food_x, food_y))
        plot_snake(gameWindow, snk_list)
        text_screen("Score: " + str(score*5), black, 5, 550)
        # gameWindow.blit(snkImage, (snake_x, snake_y))
        snake_x += velocity_x
        snake_y += velocity_y
        pygame.display.update()

    pygame.quit()
    quit()
        
def gameover():
    exit_game = False
    white = (255,255,255)

    gameoverImage = pygame.image.load("Images/gameover.jpg")
    gameoverImage = pygame.transform.scale(gameoverImage, (screenWidth, screenHeight)).convert_alpha()

    gameWindow.blit(gameoverImage, (0, 0))
    text_screen("Press Spacebar to Continue.", white, 180, 50)
    pygame.display.update()

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exit_game = True
                    gameloop()
                
                if event.key == pygame.K_RETURN:
                    exit_game = True
                    welcome()

welcome()