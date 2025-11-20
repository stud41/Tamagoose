import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tamagoose")

clock = pygame.time.Clock()
FPS = 60

BG_COLOR = (198, 219, 255)
BUTTON_COLOR = (153, 76, 0)
BUTTON_HOVER = (174, 92, 10)
TEXT_COLOR = (255, 255, 255)

goose_grosse = 1
goose_essen = 1
goose_schlafen = 1
goose_gluck = 1
goose_baden = 1

goose_1 = pygame.image.load("C:/Users/ReDI/Downloads/SMALL GOOSE PNG.png")
goose_1 = pygame.transform.scale(goose_1, (800, 600))

bg = pygame.image.load("C:/Users/ReDI/Downloads/GANZES BACKROUND.png")
bg = pygame.transform.scale(bg, (800, 600))

rect_x, rect_y, rect_width, rect_height = 250, 200, 300, 300
Menu_color = (255, 246, 189)
font = pygame.font.SysFont(None, 36)

button_rect = pygame.Rect(20, 20, 100, 50)

# Menu buttons
food_btn = pygame.image.load("C:/Users/ReDI/Downloads/FÜTTERN KNOPF.png")#pygame.Rect(200, 370, 150, 60)
food_btn = pygame.transform.scale(food_btn, (266, 200))
fake_food = pygame.Rect(280, 360, 110, 100)

sleep_btn = pygame.image.load("C:/Users/ReDI/Downloads/SCHLAFEN KNOPF.png")#(440, 370, 150, 60)
sleep_btn = pygame.transform.scale(sleep_btn, (266, 200))
fake_sleep = pygame.Rect(410, 360, 110, 100)

gluck_btn = pygame.image.load("C:/Users/ReDI/Downloads/SPIELEN KNOPF.png")#(440, 260, 150, 60)
gluck_btn = pygame.transform.scale(gluck_btn, (266, 200))
fake_gluck = pygame.Rect(280, 230, 110, 100)

bad_btn = pygame.image.load("C:/Users/ReDI/Downloads/WASCHEN KNOPF 2.png")#(400, 210, 106, 120)
bad_btn = pygame.transform.scale(bad_btn, (266, 200))
fake_bad = pygame.Rect(410, 230, 110, 100)


menu_button = False

# ---------------------- HEALTH BAR SYSTEM ---------------------
DRAIN_RATE_PER_SECOND = 2.0
DRAIN_RATE_PLAY = 3.0
DRAIN_RATE_FOOD = 2.5
DRAIN_RATE_SLEEP = 1.5

class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        if self.hp < 0:
            self.hp = 0

        ratio = self.hp / self.max_hp

        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

    def update_health(self, dt_seconds, drain_rate):
        if self.hp > 0:
            self.hp -= drain_rate * dt_seconds

# Create health bars
health_bar_play = HealthBar(550, 50, 200, 20, 100)
health_bar_food = HealthBar(550, 80, 200, 20, 100)
health_bar_bath = HealthBar(550, 110, 200, 20, 100)
health_bar_sleep = HealthBar(550, 140, 200, 20, 100)

all_health_bars = [
    health_bar_bath, health_bar_play,
    health_bar_food, health_bar_sleep
]

# ---------------------- MAIN UNIFIED GAME LOOP ---------------------
running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    mouse_pos = pygame.mouse.get_pos()

    # --- Draw background ---
    screen.blit(bg, (0, 0))
    if goose_grosse == 1:
        screen.blit(goose_1, (8, 4))

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            goose_essen += 1
            print("essen")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            goose_gluck += 1
            print("spielen")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            goose_schlafen += 1
            print("schlafen")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            goose_schlafen += 1
            print("waschen")

        # Menu button
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            menu_button = not menu_button

        # Menu interactions
        if menu_button and event.type == pygame.MOUSEBUTTONDOWN:
            if fake_food.collidepoint(event.pos):
                health_bar_food.hp = min(100, health_bar_food.hp + 20)

            if fake_sleep.collidepoint(event.pos):
                health_bar_sleep.hp = min(100, health_bar_sleep.hp + 20)

            if fake_gluck.collidepoint(event.pos):
                health_bar_play.hp = min(100, health_bar_play.hp + 20)

            if fake_bad.collidepoint(event.pos):
                health_bar_bath.hp = min(100, health_bar_bath.hp + 20)

    # ----------- UPDATE HEALTH BARS -------------
    health_bar_bath.update_health(dt, DRAIN_RATE_PER_SECOND)
    health_bar_play.update_health(dt, DRAIN_RATE_PLAY)
    health_bar_food.update_health(dt, DRAIN_RATE_FOOD)
    health_bar_sleep.update_health(dt, DRAIN_RATE_SLEEP)

    # ----------- DRAW MENU WINDOW -------------
    if menu_button:
        pygame.draw.rect(screen, Menu_color, (rect_x, rect_y, rect_width, rect_height), 0, 20)
        pygame.draw.rect(screen, (139, 69, 19), (rect_x - 5, rect_y - 5, rect_width + 10, rect_height + 10), 10, 30)

        screen.blit(food_btn, (185, 320))
        screen.blit(sleep_btn, (315, 320))
        screen.blit(gluck_btn, (185, 190))
        screen.blit(bad_btn, (315, 190))

    # ----------- DRAW MENU BUTTON -------------
    color = BUTTON_HOVER if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect)

    text_surf = font.render("MENU", True, TEXT_COLOR)
    screen.blit(text_surf, text_surf.get_rect(center=button_rect.center))

    # ----------- DRAW HEALTH BARS -------------
    for bar in all_health_bars:
        bar.draw(screen)

    pygame.display.update()

pygame.quit()


