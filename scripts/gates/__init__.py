from ..gate import Gate
from ..port import InputPort, OutputPort
from ..constants import *
from ..utils import *


class CustomGate(Gate):
    def __init__(self, name, game, position: Vector2) -> None:
        super().__init__(name, game, position)

        self.gate_data = self.load_gate_data()
        self.create_ports(INPUT, self.gate_data["input_ports"])
        self.create_ports(OUTPUT, self.gate_data["output_ports"])

    def load_gate_data(self):
        if not self.name in GATE_DATA:
            raise IndexError(f"No gate named {self.name}")

        return GATE_DATA[self.name]

    def create_ports(self, type, count):
        port_type = InputPort if type == INPUT else OutputPort
        port_list = self.input_ports if type == INPUT else self.output_ports

        offset = PORT_OFFSET + PORT_RADIUS

        for index in range(1, count + 1):
            port_list.append(
                port_type(
                    self.game,
                    self,
                    offset * index if index > count // 2 else -offset * index,
                )
            )

    def process(self):
        chosen_case = None

        for case in self.gate_data["cases"]:
            for index, input_port in enumerate(self.input_ports):
                if bool(case[index]) != is_pin_on(input_port):
                    break
            else:
                chosen_case = case

        if not chosen_case:
            return

        for index, output_port in enumerate(self.output_ports):
            output_port.enabled = bool(chosen_case[len(self.input_ports) + index])

    def update(self, input):
        super().update(input)

        self.process()
