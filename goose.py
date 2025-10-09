import pygame
pygame.init()

screen_width = 600
screen_height = 400
screen_color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Tamagoose")

game_on = True

screen_color = (198,219,255)

while game_on:
    screen.fill(screen_color)
    

#spielcode

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        screen.fill(screen_color)
        
        pygame.display.upgrade()

pygame.quit()



