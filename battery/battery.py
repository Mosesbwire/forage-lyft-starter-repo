
# battery.py
"""Abstract Battery class"""

from abc import ABC, abstractmethod


class AbstractBattery(ABC):
    """Abstract class for the Battery"""
    @abstractmethod
    def needs_service(self) -> bool:
        pass
