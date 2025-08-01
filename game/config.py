# config.py
WIDTH, HEIGHT = 800, 600
FPS = 60
SHIP_RADIUS = 20
ASTEROID_RADIUS = 30
BULLET_RADIUS = 5

ASTEROID_SPEED = 2
SHIP_THRUST = 0.15
ROTATION_SPEED = 5
BULLET_SPEED = 5

ASTEROID_SIZES = {
    "large": {"radius": 40, "speed": 0.7},
    "medium": {"radius": 25, "speed": 1.5},
    "small": {"radius": 15, "speed": 2}
}

ASTEROID_POINTS = {
    "large": 20,
    "medium": 50,
    "small": 100
}
