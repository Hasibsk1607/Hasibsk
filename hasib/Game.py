import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import time
from matplotlib.animation import FuncAnimation

# গেমের স্টেট
score = 0
snake = [(5, 5)]
direction = (0, 1)  # Initial direction (right)
fruit = (7, 7)
game_over = False

# গেমের ডেটা ট্র্যাক করতে Pandas DataFrame
game_data = {
    'Step': [],
    'Snake': [],
    'Fruit': [],
    'Score': []
}

# গেমের সীমা
grid_size = 10

# Snake Movement
def move_snake(direction):
    global snake
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake = [new_head] + snake[:-1]

# Fruit generation
def generate_fruit():
    return (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

# Check collision
def check_collision():
    head = snake[0]
    
    # Check if snake collides with itself
    if head in snake[1:]:
        return True
    
    # Check if snake goes out of bounds
    if head[0] < 0 or head[0] >= grid_size or head[1] < 0 or head[1] >= grid_size:
        return True

    return False

# Check if snake eats the fruit
def check_fruit():
    global fruit, score
    head = snake[0]
    if head == fruit:
        score += 10
        snake.append(snake[-1])  # Snake grows
        fruit = generate_fruit()
        return True
    return False

# Update game state
def update_game():
    global game_over, snake, fruit, score
    if not game_over:
        move_snake(direction)
        if check_collision():
            game_over = True
            print("Game Over!")
            return
        if check_fruit():
            pass
        
        # Add game data to DataFrame
        game_data['Step'].append(len(game_data['Step']) + 1)
        game_data['Snake'].append(snake.copy())
        game_data['Fruit'].append(fruit)
        game_data['Score'].append(score)

# Plot Snake and Fruit
def plot_game(frame):
    plt.clf()  # Clear the previous frame

    # Draw grid
    plt.xlim(-0.5, grid_size - 0.5)
    plt.ylim(-0.5, grid_size - 0.5)
    plt.grid(True)

    # Draw snake
    snake_x, snake_y = zip(*snake)
    plt.scatter(snake_y, snake_x, color='green', s=500)

    # Draw fruit
    plt.scatter(fruit[1], fruit[0], color='red', s=500)

    # Show score and step
    plt.title(f"Score: {score}")
    plt.gca().invert_yaxis()  # To match grid with the snake's movement

# Keyboard control
def on_key(event):
    global direction
    if event.key == 'up' and direction != (1, 0):
        direction = (-1, 0)
    elif event.key == 'down' and direction != (-1, 0):
        direction = (1, 0)
    elif event.key == 'left' and direction != (0, 1):
        direction = (0, -1)
    elif event.key == 'right' and direction != (0, -1):
        direction = (0, 1)

# Matplotlib animation function
def animate(frame):
    if not game_over:
        update_game()
    plot_game(frame)

# Set up the figure
fig = plt.figure(figsize=(6, 6))
fig.canvas.mpl_connect('key_press_event', on_key)

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=100, repeat=False)

# Show the plot
plt.show()
