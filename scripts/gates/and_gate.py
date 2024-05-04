from ..gate import Gate
from ..constants import *
from ..port import InputPort, OutputPort


class And(Gate):
    def __init__(self, game, position: Vector2) -> None:
        super().__init__("AND", game, position)

        self.create_ports()

    def create_ports(self):
        y_offset = PORT_RADIUS + 2

        self.input_ports.append(InputPort(self.game, self, -y_offset))
        self.input_ports.append(InputPort(self.game, self, y_offset))

        self.output_ports.append(OutputPort(self.game, self, 0))

    def update(self, input):
        super().update(input)

        output_port = self.output_ports[0]

        is_enabled = True

        for input_port in self.input_ports:
            if connection := input_port.connection:
                if not connection.source.enabled:
                    is_enabled = False
            else:
                is_enabled = False

        output_port.enabled = is_enabled
