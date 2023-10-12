

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
import unittest


class TestCarrigan(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        wear_tear_data = [0, 0.5, 1, 0.9]
        tire = CarriganTire(wear_tear_data)

        self.assertTrue(tire.needs_service())

    def test_tire_does_not_need_service(self):
        wear_tear_data = [0, 0.5, 0.8, 0.7]
        tire = CarriganTire(wear_tear_data)

        self.assertFalse(tire.needs_service())


class TestOctoprime(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        wear_tear_data = [1, 1, 1, 0.5]

        tire = OctoprimeTire(wear_tear_data)

        self.assertTrue(tire.needs_service())

    def test_tire_does_not_need_repair(self):
        wear_tear_data = [1, 1, 0.1, 0.1]

        tire = OctoprimeTire(wear_tear_data)

        self.assertFalse(tire.needs_service())
