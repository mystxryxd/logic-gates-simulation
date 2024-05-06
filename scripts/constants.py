from pygame import Vector2, Color, Surface, Rect
from pygame.constants import *
import pygame
import json

pygame.init()
pygame.font.init()

GAME_TITLE = "Logic Gates"

SCREEN_SIZE = Vector2(800, 500)

BACKGROUND_COLOR = Color(44, 44, 44)

NODE_RADIUS = 20
NODE_ENABLED_COLOR = Color(232, 49, 20)
NODE_DISABLED_COLOR = Color(28, 32, 40)

CONNECTION_COLOR = Color(229, 29, 52)

CONNECTOR_RADIUS = 5
CONNECTOR_OFFSET = 5
CONNECTOR_WIDTH = 3
CONNECTOR_COLOR = Color(4, 4, 4)

PORT_COLOR = Color(4, 4, 4)
PORT_OFFSET = 3
PORT_RADIUS = 5

GATE_LENGTH = 70
GATE_WIDTH = 50
GATE_SIZE = Vector2(GATE_LENGTH, GATE_WIDTH)

INPUT = "INPUT"
OUTPUT = "OUTPUT"

JETBRAINS_MONO = pygame.font.SysFont("Helvetica", 25)

with open("assets/gate_data.json") as data:
    GATE_DATA = json.load(data)
