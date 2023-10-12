
from battery.battery import AbstractBattery
from engine.engine import AbstractEngine
from interface.servicable import Servicable
from tire.tire import AbstractTire


class Car(Servicable):

    def __init__(self, engine: AbstractEngine, battery: AbstractBattery, tire: AbstractTire) -> None:
        self.engine: AbstractEngine = engine
        self.battery: AbstractBattery = battery
        self.tire: AbstractTire = tire

    def needs_service(self) -> bool:
        if self.battery.needs_service():
            return True
        if self.engine.needs_service():
            return True
        if self.tire.needs_service():
            return True
        return False
