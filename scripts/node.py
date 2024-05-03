from .input import Input, MouseButton
from .connection import Connection
from .connector import Connector
from .constants import *
from .utils import *
from typing import List

import pygame


class Node:
    def __init__(self, type, game, position) -> None:
        self.enabled = False

        self.type = type
        self.game = game
        self.position = position

        self.connector = Connector(self)
        self.connections: List[Connection] = []

    def is_input(self):
        return self.type == INPUT

    def has_connections(self):
        return len(self.connections) != 0

    def create_connection(self):
        if (
            self.has_connections()
            and (last_connection := self.connections[-1])
            and not last_connection.connected
        ):
            return

        self.connections.append(Connection(self))

    def update(self, input: Input):
        for connection in self.connections:
            connection.update(input)

        self.connector.update(input)

        if input.just_pressed(K_BACKSPACE) and self.has_connections():

            if (
                current_connection := self.connections[-1]
            ) and not current_connection.connected:
                connection.destroy()

        return False

    def render(self, screen: pygame.Surface):
        for connection in self.connections:
            connection.render(screen)

        self.connector.render(screen)

        pygame.draw.circle(
            screen,
            NODE_ENABLED_COLOR if self.enabled else NODE_DISABLED_COLOR,
            self.position,
            NODE_RADIUS,
        )


class InputNode(Node):
    def __init__(self, game, position: Vector2) -> None:
        super().__init__(INPUT, game, position)

    def clicked(self, input: Input) -> bool:
        if input.just_pressed(MouseButton.LEFT):
            mouse_position = input.mouse_position()

            if point_in_circle(mouse_position, self.position, NODE_RADIUS):
                return True

        return False

    def update(self, input: Input):
        super().update(input)

        if self.clicked(input):
            self.enabled = not self.enabled


class OutputNode(Node):
    def __init__(self, game, position: Vector2) -> None:
        super().__init__(OUTPUT, game, position)
