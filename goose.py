import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pressable Button Example")


BG_COLOR = (198, 219, 255)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER = (120, 120, 120)
TEXT_COLOR = (255, 255, 255)

bg = pygame.image.load("GOOSE NORMAL.jpg")
bg = pygame.transform.scale(bg, (800, 600))


button_pressed = False
first_run = True

rect_x, rect_y, rect_width, rect_height = 100, 200, 600, 300


font = pygame.font.SysFont(None, 36)

# Button setup
button_rect = pygame.Rect(20, 20, 200, 60)  # x, y, width, height

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if first_run:
        screen.blit(bg, (0,0))
        first_run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect click inside button
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            if not button_pressed:
                print("button pressed")
                button_pressed = True
                pygame.draw.rect(screen, (100, 100, 100), (rect_x, rect_y, rect_width, rect_height))
            else:
                print("this should actually delete the rectangle")
                screen.blit(bg, (0,0))
                button_pressed = False
            
        

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
