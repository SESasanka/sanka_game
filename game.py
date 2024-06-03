import pygame
import time
import random

# Initialize the game
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set the width and height of the display
display_width = 800
display_height = 600

# Set the size of the snake and the speed of movement
snake_block = 10
snake_speed = 10

# Create the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define the font for displaying the score
font_style = pygame.font.SysFont(None, 50)

# Function to display the score on the screen
def score(score):
    value = font_style.render('Score: ' + str(score), True, black)
    game_display.blit(value, [0, 0])

# Function to draw the snake on the screen
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Initial movement direction of the snake
    x1_change = 0
    y1_change = 0

    # Create an empty list to store the snake's body
    snake_list = []
    snake_length = 1

    # Generate the initial position of the food
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    # Game loop
    while not game_over:

        # If the game is over, display the game over message
        while game_close:
            game_display.fill(white)
            message('Game Over! Press Q-Quit or C-Play Again', red)
            score(snake_length - 1)
            pygame.display.update()

            # Check for user input to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Check for user input to control the snake's movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Check for collisions with the walls
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Draw the background and the food
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block, snake_block])

        # Update the snake's body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with the snake's body
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake on the screen
        snake(snake_block, snake_list)

        # Update the score
        score(snake_length - 1)

        # Update the display
        pygame.display.update()

        # Check for collisions with the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Set the frame rate
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

# Start the game loop
game_loop()
