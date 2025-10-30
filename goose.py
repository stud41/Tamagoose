import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tamagoose")


BG_COLOR = (198, 219, 255)
BUTTON_COLOR = (153,76,0)
BUTTON_HOVER = (174, 92, 10)
TEXT_COLOR = (255, 255, 255)

#1=klein, 2=mittel, 3=gross
goose_groesse = 1
goose_machen = 1
#1=wohnzimmer, 2=baden 3=schlafen
goose_groesse1 = pygame.image.load("C:/Users/ReDI User/Desktop/repo/SMALL GOOSE PNG.png")
goose_groesse1 = pygame.transform.scale(goose_groesse1, (800, 600))


bg = pygame.image.load("C:/Users/ReDI User/Desktop/repo/GANZES BACKROUND.png")
bg = pygame.transform.scale(bg, (800, 600))

button_pressed = False
first_run = True

rect_x, rect_y, rect_width, rect_height = 100, 200, 600, 300
rect_color_r, rect_color_g, rect_color_b = 255, 246, 189

font = pygame.font.SysFont(None, 36)

button_rect = pygame.Rect(20, 20, 100, 50)  # x, y, width, height

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if first_run:
        screen.blit(bg, (0,0))
        first_run = False
        if goose_groesse == 1:
            screen.blit(goose_groesse1, (8,4))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect click inside button
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            if not button_pressed:
                print("button pressed")
                button_pressed = True
                pygame.draw.rect(screen, (rect_color_r, rect_color_g, rect_color_b), (rect_x, rect_y, rect_width, rect_height))
            else:
                print("menu away")
                screen.blit(bg, (0,0))
                button_pressed = False
                first_run = True
            
        # Change color on hover
    if button_rect.collidepoint(mouse_pos):
        color = BUTTON_HOVER
    else:
        color = BUTTON_COLOR

    # Draw the button
    pygame.draw.rect(screen, color, button_rect)

    # Draw button text
    text_surf = font.render("MENU", True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)
    
    pygame.display.update()

pygame.quit()
