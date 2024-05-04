from .input import Input, MouseButton
from .constants import *
from .utils import *
from .port import InputPort, OutputPort
from typing import List

import pygame


class Gate:
    def __init__(
        self,
        name,
        game,
        position: Vector2,
    ) -> None:
        self.game = game

        self.name = name or __name__
        self.position = position
        self.rect = Rect(position, GATE_SIZE)

        self.input_ports: List[InputPort] = []
        self.output_ports: List[OutputPort] = []

        self.is_held = False

    def render_name(self, screen: Surface):
        text = JETBRAINS_MONO.render(self.name, False, Color("WHITE"))
        screen.blit(text, text.get_rect(center=self.position))

    def update_ports(self, input: Input):
        for input_port in self.input_ports:
            input_port.update(input)

        for output_port in self.output_ports:
            output_port.update(input)

    def render_ports(self, screen: Surface):
        for input_port in self.input_ports:
            input_port.render(screen)

        for output_port in self.output_ports:
            output_port.render(screen)

    def update(self, input: Input):
        if input.just_pressed(MouseButton.LEFT) and point_in_rectangle(
            input.mouse_position(), self.rect
        ):
            self.is_held = True

        if input.just_released(MouseButton.LEFT):
            self.is_held = False

        if self.is_held:
            self.position = input.mouse_position()

        self.update_ports(input)

        self.rect.center = self.position

    def render(self, screen):
        pygame.draw.rect(
            screen,
            Color(0, 255, 0),
            self.rect,
        )

        self.render_ports(screen)
        self.render_name(screen)
