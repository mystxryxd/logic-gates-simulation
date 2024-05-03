from .constants import *
from .input import Input, MouseButton
from .utils import *

import pygame


class Connector:
    def __init__(self, node) -> None:
        self.node = node

        offset = Vector2(CONNECTOR_RADIUS + NODE_RADIUS + CONNECTOR_OFFSET, 0)

        self.position = node.position + (offset if node.is_input() else -offset)

    def clicked(self, input: Input) -> bool:
        if input.just_pressed(MouseButton.LEFT):
            mouse_position = input.mouse_position()

            if point_in_circle(mouse_position, self.position, CONNECTOR_RADIUS):
                return True

        return False

    def update(self, input: Input):
        if self.clicked(input):
            self.node.create_connection()

    def render(self, screen: Surface):
        pygame.draw.line(
            screen, CONNECTOR_COLOR, self.node.position, self.position, CONNECTOR_WIDTH
        )
        pygame.draw.circle(screen, CONNECTOR_COLOR, self.position, CONNECTOR_RADIUS)
