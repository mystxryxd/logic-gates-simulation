from .input import Input, MouseButton
from .constants import *
from .utils import *

import pygame


class Connection:
    def __init__(self, game, connector) -> None:
        self.game = game

        self.connector = connector
        self.connected = False

        self.source = connector.pin
        self.destination = None

        self.start_position = connector.position
        self.end_position = connector.pin.position

    def create_connection(self, destination):
        if destination.connection:
            destination.connection.destroy()

        destination.connection = self

        self.destination = destination
        self.connected = True

    def update(self, input: Input):
        if not self.connected:
            mouse_position = input.mouse_position()

            if input.just_pressed(MouseButton.LEFT):
                if self.connector.is_node_connector():
                    for gate in self.game.gates:
                        for input_port in gate.input_ports:
                            if point_in_circle(
                                mouse_position, input_port.position, PORT_RADIUS
                            ):
                                self.create_connection(input_port)
                                return

                elif self.connector.is_port_connector():
                    for node in self.game.nodes:
                        if not node.is_input() and point_in_circle(
                            mouse_position, node.connector_position, CONNECTOR_RADIUS
                        ):
                            self.create_connection(node)
                            return

                    for gate in self.game.gates:
                        for input_port in gate.input_ports:
                            if point_in_circle(
                                mouse_position, input_port.position, PORT_RADIUS
                            ):
                                self.create_connection(input_port)
                                return

            self.end_position = mouse_position

    def render(self, screen):
        pygame.draw.line(
            screen, CONNECTION_COLOR, self.start_position, self.end_position
        )

    def destroy(self):
        self.source = None
        self.destination = None
        print("DESTROEYD")
        self.connector.destroy_connection(self)
