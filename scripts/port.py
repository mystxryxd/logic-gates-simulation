from .input import Input, MouseButton
from .connection import Connection
from .constants import *
from .utils import *

import pygame


class Port:
    def __init__(self, type, gate, y_offset) -> None:
        self.type = type
        self.gate = gate
        self.y_offset = y_offset

        self.connection: Connection = None

    def is_input(self):
        return self.type == INPUT

    def update(self, input):
        x_offset = GATE_LENGTH / 2

        self.position = self.gate.position + Vector2(
            -x_offset if self.is_input() else x_offset,
            self.y_offset,
        )

        if self.connection:
            self.connection.end_position = self.position

    def render(self, screen):
        pygame.draw.circle(screen, PORT_COLOR, self.position, PORT_RADIUS)


class InputPort(Port):
    def __init__(self, gate, y_offset) -> None:
        super().__init__(INPUT, gate, y_offset)


class OutputPort(Port):
    def __init__(self, gate, y_offset) -> None:
        self.enabled = False

        super().__init__(OUTPUT, gate, y_offset)
