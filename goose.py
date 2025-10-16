import pygame

pygame.init()

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tamagoose")

game_on = True
screen_color = (198, 219, 255)

while game_on:
    # Handle events inside the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    # Fill the screen with the background color
    screen.fill(screen_color)

    # Update the display
    pygame.display.update()

pygame.quit()





