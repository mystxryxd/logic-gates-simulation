import pygame
from .input import Input, MouseButton
from .constants import *
from .utils import *


class Connection:
    def __init__(self, node) -> None:
        self.node = node
        self.port = None
        self.connected = False

        self.start_position = node.connector.position
        self.end_position = node.position

    def update(self, input: Input):
        if not self.connected:
            mouse_position = input.mouse_position()

            if input.just_pressed(MouseButton.LEFT):
                for gate in self.node.game.gates:
                    for input_port in (
                        gate.input_ports if self.node.is_input() else gate.output_ports
                    ):
                        if not input_port.connection and point_in_circle(
                            mouse_position, input_port.position, PORT_RADIUS
                        ):
                            input_port.connection = self
                            self.connected = True

            self.end_position = mouse_position

    def render(self, screen):
        pygame.draw.line(
            screen, CONNECTION_COLOR, self.start_position, self.end_position
        )

    def destroy(self):
        self.node.connection = None
