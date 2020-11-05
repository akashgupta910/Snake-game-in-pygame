import pygame
import random

pygame.init()

pygame.mixer.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0 , 0 , 0)

# Game Window
window = pygame.display.set_mode((900,600))

# Background Image
bg_image = pygame.image.load("snake.jpg")
bg_image = pygame.transform.scale(bg_image, (900, 600)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake")



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, (x, y))

def plot_snake(window, black, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(window, black, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        window.fill((233, 229, 230))
        text_screen("Welcome to Snake", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

# Game Loop

def gameloop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 60
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(20, 900 / 2)
    food_y = random.randint(20, 600 / 2)
    score = 0
    snake_list = []
    snake_length = 1

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:

        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            window.fill(white)
            text_screen("Game Over! Press Enter to continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(20, 900 / 2)
                food_y = random.randint(20, 600 / 2)
                snake_length += 5
                if score>int(hiscore):
                    hiscore = score

            window.fill(white)
            window.blit(bg_image, (0, 0))
            text_screen("Score: " + str(score) + "  Hiscore: " + str(hiscore), red, 5, 5)
            pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(window, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
# gameloop()