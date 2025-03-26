import pygame

pygame.init()

W, H = 800, 800
sc = pygame.display.set_mode((W, H))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (252, 154, 8)
YELLOW = (252, 248, 3)
PINK = (252, 3, 252)
PURPLE = (169, 3, 252)
GRAY = (206, 204, 207)
colors = {'white': WHITE, 'black': BLACK, 'red': RED, 'green': GREEN, 'blue': BLUE, 'orange': ORANGE, 'yellow': YELLOW, 'pink': PINK, 'purple': PURPLE, 'gray': GRAY}

eraser = pygame.image.load('C:\\Users\\mierc\\OneDrive\\Рабочий стол\\PP2\\lab_8_pp2\\PygameTutorial_3_0\\Eraser.png').convert_alpha()
eraser = pygame.transform.scale(eraser, (eraser.get_width() // 5, eraser.get_height() // 5))
eraser_rect = eraser.get_rect(center=(700, 70))
eraser2 = pygame.transform.scale(eraser, (eraser.get_width() * 2, eraser.get_height() * 2))
current_color = RED

drawed = []
sc.fill(WHITE)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 15)
is_erase = False
is_visible = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for color_name, color_rect in [("yellow", YELLOW), ("green", GREEN), ("red", RED), ("blue", BLUE), ("orange", ORANGE), ("pink", PINK), ("purple", PURPLE), ("black", BLACK)]:
                if globals()[f"color_{color_name}"].collidepoint(event.pos):
                    current_color = color_rect
            if eraser_rect.collidepoint(event.pos):
                is_visible = not is_visible
                is_erase = not is_erase
    
    sc.fill(WHITE)
    pressed = pygame.mouse.get_pressed()
    if pressed[0] and 0 <= pygame.mouse.get_pos()[0] <= 800 and 183 <= pygame.mouse.get_pos()[1] <= 800:
        drawed.append((pygame.mouse.get_pos(), current_color))
    
    pygame.mouse.set_visible(is_visible)
    for pos, color in drawed:
        pygame.draw.circle(sc, color, pos, 5)
    
    if is_erase:
        sc.blit(eraser2, pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            drawed = [(pos, color) for pos, color in drawed if ((pos[0] - mx) ** 2 + (pos[1] - my) ** 2) ** 0.5 > 10]
    
    pygame.draw.rect(sc, GRAY, (50, 30, 100, 100), 3)
    pygame.draw.rect(sc, current_color, (55, 35, 90, 90))
    
    for i, (name, color) in enumerate(colors.items()):
        x, y = (290 + (i % 4) * 70, 30 + (i // 4) * 70)
        globals()[f"color_{name}"] = pygame.draw.rect(sc, color, (x + 5, y + 5, 40, 40))
        pygame.draw.rect(sc, GRAY, (x, y, 50, 50), 3)
    
    pygame.draw.line(sc, BLACK, (0, 180), (800, 180), 3)
    pygame.draw.line(sc, BLACK, (270, 180), (270, 0), 3)
    pygame.draw.line(sc, BLACK, (630, 180), (630, 0), 3)
    
    sc.blit(font.render("Now using", True, BLACK), (60, 10))
    sc.blit(font.render("Colors", True, BLACK), (400, 10))
    sc.blit(font.render("Tools", True, BLACK), (660, 10))
    
    sc.blit(eraser, eraser_rect)
    pygame.display.update()
    clock.tick(60)