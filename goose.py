import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pressable Button Example")

# Colors
BG_COLOR = (173, 216, 230)  # Hellblau (light blue)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER = (120, 120, 120)
TEXT_COLOR = (255, 255, 255)
RECT_COLOR = (100, 100, 100)
RECT_HIDE_COLOR = BG_COLOR  # Farbe zum "Löschen" des Rechtecks

# States
button_pressed = False

# Rectangle setup
rect_x, rect_y, rect_width, rect_height = 100, 200, 600, 300

# Font setup
font = pygame.font.SysFont(None, 36)

# Button setup
button_rect = pygame.Rect(20, 20, 200, 60)  # x, y, width, height

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect click inside button
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            button_pressed = not button_pressed
            if button_pressed:
                print("button pressed")
            else:
                print("rectangle hidden")

    # Fill background
    screen.fill(BG_COLOR)

    # Draw rectangle if button is pressed
    if button_pressed:
        pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, rect_width, rect_height))

    # Change button color on hover
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

    # Update the screen
    pygame.display.update()

pygame.quit()
