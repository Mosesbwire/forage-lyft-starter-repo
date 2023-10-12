
from battery.battery import AbstractBattery
from engine.engine import AbstractEngine
from interface.servicable import Servicable


class Car(Servicable):

    def __init__(self, engine: AbstractEngine, battery: AbstractBattery) -> None:
        self.engine: AbstractEngine = engine
        self.battery: AbstractBattery = battery

    def needs_service(self) -> bool:
        return self.battery.needs_service() or self.engine.needs_service()
