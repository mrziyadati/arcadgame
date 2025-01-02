import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Аркада: Уклоняйся от объектов!")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Игровые настройки
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10

falling_object_width = 50
falling_object_height = 50
falling_object_speed = 5
falling_objects = []

# Шрифт для текста
font = pygame.font.SysFont(None, 36)

# Функция для отображения текста
def display_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Основной игровой цикл
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Генерация падающих объектов
    if random.randint(1, 20) == 1:  # Вероятность появления нового объекта
        falling_objects.append([random.randint(0, screen_width - falling_object_width), 0])

    # Обновление позиции падающих объектов
    for obj in falling_objects[:]:
        obj[1] += falling_object_speed
        if obj[1] > screen_height:
            falling_objects.remove(obj)

    # Проверка на столкновение
    for obj in falling_objects:
        if (player_x < obj[0] + falling_object_width and player_x + player_width > obj[0] and
            player_y < obj[1] + falling_object_height and player_y + player_height > obj[1]):
            game_over = True

    # Отображение
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    for obj in falling_objects:
        pygame.draw.rect(screen, RED, (obj[0], obj[1], falling_object_width, falling_object_height))

    display_text("Избегай объектов!", 10, 10, (0, 0, 0))

    pygame.display.update()

    clock.tick(60)  # Обновляем экран 60 раз в секунду

pygame.quit()
sys.exit()
