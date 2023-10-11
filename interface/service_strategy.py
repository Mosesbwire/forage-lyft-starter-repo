
from abc import ABC, abstractmethod
from car.car import Car


class ServiceStrategy(ABC):

    @abstractmethod
    def service_criteria(self, car: Car) -> bool:
        pass
