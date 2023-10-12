
from datetime import datetime as dt
import datetime
from dateutil import parser
from car.car_factory import CarFactory
import unittest
from unittest.mock import Mock


class TestCarFactory(unittest.TestCase):

    def test_car_is_calliope(self):
        last_service = 3.5
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)
        current_mileage = 40000
        last_mileage = 0
        tire_data = [0.9, 0.5, 1, 0.2]
        car = CarFactory.create_calliope(
            current_date, last_service_date, current_mileage, last_mileage, tire_data)

        self.assertTrue(car.needs_service())

    def test_car_is_glissade(self):
        last_service = 3.5
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)
        current_mileage = 60000
        last_mileage = 0
        tire_data = [0.9, 0.5, 1, 0.2]

        car = CarFactory.create_calliope(
            current_date, last_service_date, current_mileage, last_mileage, tire_data)

        self.assertTrue(car.needs_service())

    def test_car_is_palindrome(self):
        current_date = dt.now()
        last_service_date = parser.parse("January 1, 2020 8:00 AM")
        warning_light = True
        tire_data = [0.9, 0.5, 1, 0.2]

        car = CarFactory.create_palindrome(
            current_date, last_service_date, warning_light, tire_data)

        self.assertTrue(car.needs_service())

    def test_car_is_rorschach(self):
        last_service = 4.5
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)
        current_mileage = 60000
        last_mileage = 0
        tire_data = [1, 1, 1, 0.2]

        car = CarFactory.create_rorschach(
            current_date, last_service_date, current_mileage, last_mileage, tire_data)

        self.assertTrue(car.needs_service())

    def test_car_is_thovex(self):
        last_service = 4.5
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)
        current_mileage = 35000
        last_mileage = 0
        tire_data = [1, 1, 1, 0.2]

        car = CarFactory.create_rorschach(
            current_date, last_service_date, current_mileage, last_mileage, tire_data)

        self.assertTrue(car.needs_service())
