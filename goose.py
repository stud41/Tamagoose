import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pressable Button Example")


BG_COLOR = (198, 219, 255)
BUTTON_COLOR = (153,76,0)
BUTTON_HOVER = (174, 92, 10)
TEXT_COLOR = (255, 255, 255)

# 1=klein, 2=mittel, 3=groß
goose_grosse = 1

goose_1 = pygame.image.load("C:/Users/ReDI User/Pictures/spiel_!!/SMALL GOOSE PNG.png")
goose_1 = pygame.transform.scale(goose_1, (800, 600))
# 1=normal, 2=baden, 3=schlafen, 4=essen
goose_machen = 1

goose_essen = 1
goose_schlafen = 1
goose_gluck = 1
goose_baden = 1

bg = pygame.image.load("C:/Users/ReDI User/Desktop/GANZES BACKROUND.png")
bg = pygame.transform.scale(bg, (800, 600))

button_pressed = False
first_run = True

rect_x, rect_y, rect_width, rect_height = 100, 200, 600, 300
Menu_color = 255, 246, 189

font = pygame.font.SysFont(None, 36)

button_rect = pygame.Rect(20, 20, 100, 50)# x, y, width, height

food_rect = pygame.image.load("C:/Users/ReDI User/Downloads/FÜTTERN KNOPF.png")#pygame.Rect(200, 370, 150, 60)
food_rect = pygame.transform.scale(food_rect, (266, 200))
fake_food = pygame.Rect(160, 300, 266, 200)
sleep_rect = pygame.Rect(440, 370, 150, 60)
gluck_rect = pygame.Rect(440, 260, 150, 60)
bad_rect = pygame.Rect(200, 260, 150, 60)

menu_button = False

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    #mouse_pressed = pygame.mouse.get_pressed()

    if first_run:
        screen.blit(bg, (0,0))
        first_run = False
        if goose_grosse == 1:
            screen.blit(goose_1, (8, 4))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect click inside button
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            if not button_pressed:
                #print("button pressed")
                button_pressed = True
                pygame.draw.rect(screen, (Menu_color), (rect_x, rect_y, rect_width, rect_height), 0, 20)
                pygame.draw.rect(screen, (139, 69, 19), (rect_x-5, rect_y-5, rect_width+10, rect_height+10), 10, 30)
                menu_button = True
            else:
                #print("this should actually delete the rectangle")
                screen.blit(bg, (0,0))
                button_pressed = False
                menu_button = False
                first_run = True
                
        if menu_button == True:
            screen.blit(food_rect, (160, 300))
            if event.type == pygame.MOUSEBUTTONDOWN and fake_food.collidepoint(event.pos):
                goose_essen += 1
                    
            pygame.draw.rect(screen, (238, 154, 73), sleep_rect)
            if event.type == pygame.MOUSEBUTTONDOWN and sleep_rect.collidepoint(event.pos):
                goose_schlafen += 1
                
            pygame.draw.rect(screen, (238, 154, 73), gluck_rect)
            if event.type == pygame.MOUSEBUTTONDOWN and gluck_rect.collidepoint(event.pos):
                goose_gluck += 1
                
            pygame.draw.rect(screen, (238, 154, 73), bad_rect)
            if event.type == pygame.MOUSEBUTTONDOWN and bad_rect.collidepoint(event.pos):
                goose_baden += 1
    
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

