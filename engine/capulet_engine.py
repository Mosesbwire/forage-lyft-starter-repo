#!/usr/bin/env python3
# capulet_engine.py

from typing import Any
from engine.engine import AbstractEngine


class CapuletEngine(AbstractEngine):

    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage: int = last_service_mileage
        self.current_mileage: int = current_mileage

    def set_last_service_mileage(self):
        self.last_service_mileage = self.current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000
