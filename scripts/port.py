from .input import Input
from .connector import PortConnector
from .connection import Connection
from .constants import *
from .utils import *

import pygame


class Port:
    def __init__(self, type, game, gate, y_offset) -> None:
        self.game = game
        self.type = type
        self.gate = gate
        self.y_offset = y_offset

        self.position = self.update_position()

    def is_input(self):
        return self.type == INPUT

    def update_position(self):
        x_offset = GATE_LENGTH / 2

        return self.gate.position + Vector2(
            -x_offset if self.is_input() else x_offset,
            self.y_offset,
        )

    def update(self, _input):
        self.position = self.update_position()

    def render(self, screen):
        pygame.draw.circle(screen, PORT_COLOR, self.position, PORT_RADIUS)


class InputPort(Port):
    def __init__(self, game, gate, y_offset) -> None:
        super().__init__(INPUT, game, gate, y_offset)

        self.connection: Connection = None

    def update(self, input: Input):
        super().update(input)

        if self.connection:
            self.connection.end_position = self.position


class OutputPort(Port):
    def __init__(self, game, gate, y_offset) -> None:
        super().__init__(OUTPUT, game, gate, y_offset)

        self.enabled = False
        self.connector = PortConnector(self, game)

    def update(self, input):
        self.connector.update(input)

        super().update(input)

    def render(self, screen):
        self.connector.render(screen)

        super().render(screen)
