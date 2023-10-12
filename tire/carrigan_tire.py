

from tire.tire import AbstractTire


class CarriganTire(AbstractTire):

    def __init__(self, wear_tear_data: list[float]):
        self.wear_tear_data: list[float] = wear_tear_data

    def needs_service(self):
        threshold = 0.9
        for data in self.wear_tear_data:
            if data == threshold:
                return True
        return False
