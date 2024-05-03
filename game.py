from scripts.constants import *
from scripts.input import Input
from scripts.node import InputNode, OutputNode
from scripts.gates import And
import pygame
import sys


class Game:
    def __init__(self) -> None:
        self.is_running = False
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        self.input = Input(self)
        self.nodes = []
        self.gates = []

        self.set_title()
        self.create_gates()
        self.create_input_nodes()

    def create_gates(self):
        center = SCREEN_SIZE / 2

        self.gates.append(And(center))

    def create_input_nodes(self):
        center = SCREEN_SIZE / 2

        y_offset = 10 + NODE_RADIUS
        x_offset = 20 + NODE_RADIUS

        self.nodes.append(InputNode(self, center + (-center.x + x_offset, y_offset)))
        self.nodes.append(InputNode(self, center + (-center.x + x_offset, -y_offset)))
        self.nodes.append(OutputNode(self, center + (center.x - x_offset, 0)))

    def set_title(self):
        pygame.display.set_caption(GAME_TITLE)

    def update(self):
        for node in self.nodes:
            node.update(self.input)

        for gate in self.gates:
            gate.update(self.input)

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)

        for node in self.nodes:
            node.render(self.screen)

        for gate in self.gates:
            gate.render(self.screen)

        pygame.display.flip()

    def quit(self):
        self.is_running = False

        pygame.quit()
        sys.exit()

    def run(self):
        self.is_running = True

        while self.is_running:
            self.input.process()

            self.update()
            self.render()

            self.input.flush()


Game().run()
