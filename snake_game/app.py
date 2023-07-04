import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Определение размеров окна
window_width = 800
window_height = 600

# Определение размеров блока и скорости змейки
block_size = 20
snake_speed = 15

# Создание окна
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

# Определение класса змейки
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((window_width / 2), (window_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = green

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*block_size)) % window_width), (cur[1] + (y*block_size)) % window_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((window_width / 2), (window_height / 2))]
        self.direction = random.choice([up, down, left, right])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], block_size, block_size))

# Определение класса еды
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (window_width // block_size)-1) * block_size,
                         random.randint(0, (window_height // block_size)-1) * block_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], block_size, block_size))

# Определение направлений движения
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# Основная функция игры
def game_loop():
    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != down:
                    snake.direction = up
                elif event.key == pygame.K_DOWN and snake.direction != up:
                    snake.direction = down
                elif event.key == pygame.K_LEFT and snake.direction != right:
                    snake.direction = left
                elif event.key == pygame.K_RIGHT and snake.direction != left:
                    snake.direction = right

        snake.update()

        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        window.fill(black)
        snake.draw(window)
        food.draw(window)

        pygame.display.update()
        clock.tick(snake_speed)

# Запуск игры
game_loop()