

from tire.tire import AbstractTire


class OctoprimeTire(AbstractTire):

    def __init__(self, wear_tear_data: list[float]):
        self.wear_tear_data: list[float] = wear_tear_data

    def needs_service(self):
        return sum(self.wear_tear_data) >= 3
