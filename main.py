import pygame
import random

screen_width = 640
screen_height = 480

background_color = (0, 0, 0)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

block_size = 20

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

def show_message(text):
    font = pygame.font.Font(None, 36)
    message = font.render(text, True, snake_color)
    screen.blit(message, (screen_width/2 - message.get_width()/2, screen_height/2 - message.get_height()/2))
    pygame.display.update()
    pygame.time.wait(2000)

def snake_game():
    head_x = screen_width / 2
    head_y = screen_height / 2

    dx = 0
    dy = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -block_size
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = block_size

        head_x += dx
        head_y += dy

        if head_x < 0 or head_x >= screen_width or head_y < 0 or head_y >= screen_height:
            game_over = True

        screen.fill(background_color)

        pygame.draw.rect(screen, food_color, [food_x, food_y, block_size, block_size])

        snake.append((head_x, head_y))

        if head_x == food_x and head_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0
            length += 1

        if len(snake) > length:
            del snake[0]

        if any(segment == snake[-1] for segment in snake[:-1]):
            game_over = True

        for segment in snake:
            pygame.draw.rect(screen, snake_color, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        clock.tick(10)

    show_message("Game Over")

    pygame.quit()

snake_game()