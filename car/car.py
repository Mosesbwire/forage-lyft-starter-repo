
from battery.battery import AbstractBattery
from engine.engine import AbstractEngine
from interface.servicable import Servicable


class Car(Servicable):
    battery: AbstractBattery
    engine: AbstractEngine

    def set_engine(self, engine: AbstractEngine) -> None:
        self.engine = engine

    def set_battery(self, battery: AbstractBattery) -> None:
        self.battery = battery

    def get_battery(self):
        return self.battery

    def get_engine(self):
        return self.engine

    def needs_service(self) -> bool:
        return self.battery.needs_service() or self.engine.needs_service()
