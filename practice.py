import pygame

pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Рисование круга")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Переменные для рисования
start_pos = None
drawing = False

# Заливка фона
screen.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if start_pos:
                end_pos = event.pos
                dx = abs(end_pos[0] - start_pos[0])
                dy = abs(end_pos[1] - start_pos[1])
                radius = int(((dx ** 2 + dy ** 2) ** 0.5) / 2)
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(screen, BLACK, center, radius, 5)
            drawing = False

    pygame.display.update()
