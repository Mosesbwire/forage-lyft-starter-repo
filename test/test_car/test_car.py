
from car.car import Car
import unittest
from unittest.mock import Mock


class TestCar(unittest.TestCase):

    def test_car_needs_service(self):
        engine_mock = Mock()
        battery_mock = Mock()

        car = Car(engine_mock, battery_mock)

        engine_mock.needs_service.return_value = True
        battery_mock.needs_service.return_value = False

        self.assertTrue(car.needs_service())
        engine_mock.needs_service.assert_called_once()
        battery_mock.needs_service.assert_called_once()

    def test_car_does_not_need_service(self):
        engine_mock = Mock()
        battery_mock = Mock()

        car = Car(engine_mock, battery_mock)

        engine_mock.needs_service.return_value = False
        battery_mock.needs_service.return_value = False

        self.assertFalse(car.needs_service())
        engine_mock.needs_service.assert_called_once()
        battery_mock.needs_service.assert_called_once()
