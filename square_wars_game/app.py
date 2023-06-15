import pygame
import random
import sys
import json
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Настройка поле игры
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Square Wars")

# Настраиваем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Настрайка аттрибутов пользователя
player_size = 50
player_x = window_width // 2 - player_size // 2
player_y = window_height - player_size - 10
player_speed = 5

# Настройка аттрибутов вражеских сил
enemy_size = 50
enemy_x = random.randint(0, window_width - enemy_size)
enemy_y = -enemy_size
enemy_speed = 3
enemy_acceleration = 0.005

# Настройка общих переменных
score = 0
max_score = 0
font = pygame.font.Font(None, 36)

# Настройка времени игры
clock = pygame.time.Clock()

game_over = False
play_again = False

# Загрузка сохраненного рекорда по очкам из JSON файла
try:
    with open("game_record.json", "r") as file:
        record = json.load(file)
        max_score = record["max_score"]
except FileNotFoundError:
    pass

# Game Loop -> Цикл событий игры
def game_loop():
    # Задача глобальных переменных
    global game_over, play_again, max_score

    game_over = True

    # Обновление значения максимального очка:
    if score > max_score:
        max_score = score

    # Обновление значении максимального очка в JSON файле:
    record = {"max_score": max_score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    with open("game_record.json", "w") as file:
        json.dump(record, file)

    # Цикл событий во время проигрыша
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        window.fill(BLACK)
        game_over_text = font.render("Game Over! Your Score: " + str(score), True, WHITE)
        window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))

        # Настройка и вывод кнопки "Играть снова"
        play_again_button = pygame.Rect(window_width // 2 - 75, window_height // 2 + 50, 150, 50)
        pygame.draw.rect(window, WHITE, play_again_button)
        play_again_text = font.render("Play Again", True, BLACK)
        window.blit(play_again_text, (window_width // 2 - play_again_text.get_width() // 2, window_height // 2 + 75 - play_again_text.get_height() // 2))

        # Перемещение позиции курсора на кнопку "Играть снова"
        mouse_pos = pygame.mouse.get_pos()
        if play_again_button.collidepoint(mouse_pos):
            pygame.draw.rect(window, RED, play_again_button, 3)
            if pygame.mouse.get_pressed()[0] == 1:
                play_again = True
                game_over = False
        else:
            pygame.draw.rect(window, BLACK, play_again_button, 3)

        # Обновление фрейма
        pygame.display.update()

# Основной цикл игры
while not game_over:
    # Настройка методов выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Контроллер: Управление кнопками "->" & "<-" для движения
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_size:
        player_x += player_speed

    window.fill(BLACK)

    enemy_y += enemy_speed
    enemy_speed += enemy_acceleration

    # Создание нового врага, если предыдущий пропал из поле игры
    if enemy_y > window_height:
        enemy_x = random.randint(0, window_width - enemy_size)
        enemy_y = -enemy_size
        score += 1
        enemy_speed += enemy_acceleration

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    # Если фигура противника коснулась фигуры игрока, то возвращаемся в game_loop() -> для учета поражения
    if player_rect.colliderect(enemy_rect):
        game_loop()

    pygame.draw.rect(window, RED, enemy_rect)
    pygame.draw.rect(window, WHITE, player_rect)
    
    # Динамично показываем статистику игры пользователя: "Score" - нынешнее количество очков, "Record" - рекордное количество очков
    score_text = font.render("Score: " + str(score), True, WHITE)
    max_score_text = font.render("Record: " + str(max_score), True, '#FFD700')
    window.blit(score_text, (10, 10))
    window.blit(max_score_text, (10, 40))

    # Обновление фрейма
    pygame.display.update()

    # FPS (Frame Per Second) Limit
    clock.tick(60)

    if play_again:
        # Вернуть в изначальное состояние значения переменных
        play_again = False
        game_over = False
        score = 0
        enemy_speed = 3
        enemy_x = random.randint(0, window_width - enemy_size)
        enemy_y = -enemy_size

# Заключение программы - выход из игры
pygame.quit()
sys.exit()
