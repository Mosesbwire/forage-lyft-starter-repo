#!/usr/bin/env python3
# battery.py

from abc import ABC, abstractmethod


class AbstractBattery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass
