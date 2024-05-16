import cv2
import map
import time
import random
import circle
import player
import painter
import physics
import numpy as np

print('Futebots! Genetic algorithms for football agents.')

# Globals
start = time.time()
end = time.time()
elapsed_time = 0.033  # Just initializing the variable
target_elapsed_time = 0.033  # Aiming at a target realtime fps (30fps)
exit = False
generation = 0

# Create game components
# Field
field = map.Map(1000, 700, 100, 250)

# Skin colors in RGB
skin_colors = [
    (196, 223, 255),
    (168, 203, 234),
    (171, 226, 247),
    (100, 139, 172),
    (60, 97, 148),
    (77, 100, 153),
    (30, 40, 63)
]

# Hair colors in RGB
hair_colors = [
    (30, 40, 45),
    (60, 75, 80),
    (80, 75, 60),
    (10, 40, 50),
    (5, 10, 15)
]

def reset_ball():
    return circle.Circle(15, int((field.margin + field.width)/2), int((field.margin + field.height)/2), 0)

ball = reset_ball()
scored = 0
goals1 = 0
goals2 = 0
total_time = 0
freeze_time = 0

def simulate_physics(target_elapsed_time, field, players, ball):
    for p in players:
        physics.move_player(p, field, players, target_elapsed_time)

    goal = physics.move_ball(ball, field, players, target_elapsed_time)
    return goal

def paint(players, ball, image):
    painter.paint_ball(image, ball)
    for p in players:
        painter.paint_player(image, p)
    painter.paint_score(image, goals1, goals2, field, total_time)
    cv2.imshow('Futebots! Genetic algorithms for football agents.', image)

def update_score(scored, goals1, goals2):
    if scored != 0:
        # If a goal was scored, reset the ball and the players
        players = reset_players()
        ball = reset_ball()

        if scored == 1:
            goals1 += 1
        elif scored == -1:
            goals2 += 1

        scored = 0

    return goals1, goals2

def reset_players():
    # Definindo as posições iniciais para o time vermelho (esquerda) e o time verde (direita)
    start_pos_red = [
        np.array((int(field.margin / 2 + field.width * 0.2), int(field.margin / 2 + field.height * 0.25))),
        np.array((int(field.margin / 2 + field.width * 0.3), int(field.margin / 2 + field.height * 0.5))),
        np.array((int(field.margin / 2 + field.width * 0.2), int(field.margin / 2 + field.height * 0.75)))
    ]
    start_pos_green = [
        np.array((int(field.margin / 2 + field.width * 0.8), int(field.margin / 2 + field.height * 0.25))),
        np.array((int(field.margin / 2 + field.width * 0.7), int(field.margin / 2 + field.height * 0.5))),
        np.array((int(field.margin / 2 + field.width * 0.8), int(field.margin / 2 + field.height * 0.75)))
    ]

    # Inicializar lista de jogadores
    players = []

    # Criar jogadores do time vermelho (Team 1)
    for i in range(3):
        p = player.Player(
            circle.Circle(random.randint(20, 100), start_pos_red[i][0], start_pos_red[i][1], random.uniform(0, 2 * np.pi)),
            1,  # Time 1 (vermelho)
            random.choice(skin_colors),
            random.choice(hair_colors),
            random.uniform(30, 70),
            random.uniform(50, 150),
            random.uniform(-0.002, 0.002),
            random.uniform(30, 90),
            random.uniform(200, 500)
        )
        players.append(p)

    # Criar jogadores do time verde (Team 2)
    for i in range(3):
        p = player.Player(
            circle.Circle(random.randint(20, 100), start_pos_green[i][0], start_pos_green[i][1], random.uniform(0, 2 * np.pi)),
            2,  # Time 2 (verde)
            random.choice(skin_colors),
            random.choice(hair_colors),
            random.uniform(30, 70),
            random.uniform(50, 150),
            random.uniform(-0.002, 0.002),
            random.uniform(30, 90),
            random.uniform(200, 500)
        )
        players.append(p)

    return players



# Main game loop
while not exit:

    # Create the image from the field
    image = painter.create_field_image(field)

    if freeze_time == 0:
        players = reset_players()
        ball = reset_ball()

    if freeze_time >= 1:

        # Simulate the game components
        scored = simulate_physics(target_elapsed_time, field, players, ball)
        goals1, goals2 = update_score(scored, goals1, goals2)

        # Paint the game components
        paint(players, ball, image)

    freeze_time += 1

    if scored != 0:
        scored = 0
        freeze_time = -60

    # Time management
    end = time.time()
    elapsed_time = end - start
    time.sleep(max(0, target_elapsed_time - elapsed_time))
    if freeze_time >= 1:
        total_time += target_elapsed_time
    start = time.time()

    # Capture key press
    if cv2.waitKey(1) == 27:  # esc keys
        exit = True