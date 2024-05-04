from .input import Input, MouseButton
from .connection import Connection
from .constants import *
from .utils import *
from typing import List

import pygame


class Connector:
    def __init__(self, pin, game) -> None:
        self.game = game

        self.pin = pin
        self.connections: List[Connection] = []

    def is_node_connector(self):
        return isinstance(self, NodeConnector)

    def is_port_connector(self):
        return isinstance(self, PortConnector)

    def has_connections(self):
        return len(self.connections) != 0

    def create_connection(self):
        if (
            self.has_connections()
            and (last_connection := self.connections[-1])
            and not last_connection.connected
        ):
            return

        self.connections.append(Connection(self.game, self))

    def clicked(self, input: Input) -> bool:
        if input.just_pressed(MouseButton.LEFT):
            mouse_position = input.mouse_position()

            if point_in_circle(mouse_position, self.position, CONNECTOR_RADIUS):
                return True

        return False

    def update(self, input: Input):
        for connection in self.connections:
            connection.update(input)

        if input.just_pressed(K_BACKSPACE) and self.has_connections():
            if (
                current_connection := self.connections[-1]
            ) and not current_connection.connected:
                current_connection.destroy()
                self.connections.pop()

        if self.clicked(input):
            self.create_connection()

    def render(self, screen: Surface):
        for connection in self.connections:
            connection.render(screen)


class NodeConnector(Connector):
    def __init__(self, node, game) -> None:
        super().__init__(node, game)

    def update(self, input: Input):
        self.position = self.pin.connector_position

        super().update(input)

    def render(self, screen: Surface):
        super().render(screen)


class PortConnector(Connector):
    def __init__(self, port, game) -> None:
        super().__init__(port, game)

        self.position = port.position

    def update(self, input: Input):
        self.position = self.pin.position

        for connection in self.connections:
            connection.start_position = self.position

        super().update(input)

    def render(self, screen: Surface):
        super().render(screen)
