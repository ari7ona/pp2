import pygame
import psycopg2
import sys
import random
from datetime import datetime

# Function to connect to the database
def connect_to_db():
    conn = psycopg2.connect(
        dbname="pp2",
        user="pp2",
        password="Hjk12345",
        host="localhost",
        port="54321"
    )
    return conn

# Function to create tables if they don't exist
def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            score_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(user_id),
            score INT,
            level INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

# Function to get user's current level
def get_user_level(username, cursor):
    cursor.execute("SELECT level FROM user_scores WHERE user_id = (SELECT user_id FROM users WHERE username = %s) ORDER BY timestamp DESC LIMIT 1", (username,))
    level = cursor.fetchone()
    if level:
        return level[0]
    else:
        return 1  # Default to level 1 if no level is found

# Function to update user's score and level
def update_user_score(username, score, level, cursor):
    cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    cursor.execute("INSERT INTO user_scores (user_id, score, level) VALUES ((SELECT user_id FROM users WHERE username = %s), %s, %s)", (username, score, level))

# Function to save game state
def save_game_state(username, score, level):
    conn = connect_to_db()
    cursor = conn.cursor()
    update_user_score(username, score, level, cursor)
    conn.commit()
    conn.close()

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Direction Constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = RIGHT

    def move(self):
        x, y = self.body[0]
        x += self.direction[0] * CELL_SIZE
        y += self.direction[1] * CELL_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        x, y = self.body[-1]
        self.body.append((x, y))

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        for part in self.body[1:]:
            if part == (x, y):
                return True
        return False

# Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        self.y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0
    level = 1

    conn = connect_to_db()
    cursor = conn.cursor()
    create_tables(cursor)
    username = input("Enter your username: ")
    level = get_user_level(username, cursor)
    conn.close()

    # Game loop
    running = True
    paused = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        if paused:
            continue

        # Move snake
        snake.move()

        # Check for collisions
        if snake.check_collision():
            running = False
            print("Game Over!")

        # Check for food eaten
        if snake.body[0] == (food.x, food.y):
            snake.grow()
            food = Food()
            score += 10
            if score % 50 == 0:
                level += 1

        # Draw everything
        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

        # Control the game speed
        clock.tick(10 + level * 2)

    save_game_state(username, score, level)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
