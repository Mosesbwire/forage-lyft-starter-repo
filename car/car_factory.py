
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car.car import Car
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:

    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data: list[float]) -> Car:
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        tire = CarriganTire(tire_data)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data: list[float]) -> Car:
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        tire = CarriganTire(tire_data)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, tire_data: list[float]) -> Car:
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(last_service_date, warning_light_on)
        tire = CarriganTire(tire_data)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data: list[float]) -> Car:
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        tire = OctoprimeTire(tire_data)
        car = Car(engine, battery, tire)

        return car

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data: list[float]) -> Car:
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        tire = OctoprimeTire(tire_data)
        car = Car(engine, battery, tire)

        return car
