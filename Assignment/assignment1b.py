import random

# List of balls
balls = ['black'] * 3 + ['yellow'] * 4 + ['white'] * 5

# Simulate picking a ball
picked_ball = random.choice(balls)

# Check if the picked ball is yellow and print a message
if picked_ball == 'yellow':
    print(f"You picked a {picked_ball} ball! Great choice!")
else:
    print(f"You picked a {picked_ball} ball. Try again to pick a yellow one!")