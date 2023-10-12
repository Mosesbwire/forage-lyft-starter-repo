
from abc import ABC, abstractmethod


class AbstractTire(ABC):

    @abstractmethod
    def needs_service(self):
        pass
