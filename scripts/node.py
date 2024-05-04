from .input import Input, MouseButton
from .connector import NodeConnector
from .constants import *
from .utils import *

import pygame


class Node:
    def __init__(self, type, game, position) -> None:
        self.enabled = False

        self.type = type
        self.game = game
        self.position = position

        offset = Vector2(CONNECTOR_RADIUS + NODE_RADIUS + CONNECTOR_OFFSET, 0)
        self.connector_position = position + (offset if self.is_input() else -offset)

    def is_input(self):
        return self.type == INPUT

    def update(self, _input):
        pass

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, CONNECTOR_COLOR, self.connector_position, CONNECTOR_RADIUS
        )

        pygame.draw.line(
            screen,
            CONNECTOR_COLOR,
            self.position,
            self.connector_position,
            CONNECTOR_WIDTH,
        )

        pygame.draw.circle(
            screen,
            NODE_ENABLED_COLOR if self.enabled else NODE_DISABLED_COLOR,
            self.position,
            NODE_RADIUS,
        )


class InputNode(Node):
    def __init__(self, game, position: Vector2) -> None:
        super().__init__(INPUT, game, position)

        self.connector = NodeConnector(self, game)

    def clicked(self, input: Input) -> bool:
        if input.just_pressed(MouseButton.LEFT):
            mouse_position = input.mouse_position()

            if point_in_circle(mouse_position, self.position, NODE_RADIUS):
                return True

        return False

    def update(self, input: Input):
        self.connector.update(input)

        if self.clicked(input):
            self.enabled = not self.enabled

    def render(self, screen: Surface):
        self.connector.render(screen)

        super().render(screen)


class OutputNode(Node):
    def __init__(self, game, position: Vector2) -> None:
        super().__init__(OUTPUT, game, position)

        self.connection = None

    def update(self, input):
        if connection := self.connection:
            self.enabled = connection.connector.pin.enabled
