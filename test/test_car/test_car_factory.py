
from datetime import datetime
from dateutil import parser
from car.car_factory import CarFactory
import unittest
from unittest.mock import Mock


class TestCarFactory(unittest.TestCase):

    def test_car_is_calliope(self):
        current_date = datetime.now()
        last_service_date = parser.parse("January 1, 2020 8:00 AM")
        current_mileage = 40000
        last_mileage = 0
        car = CarFactory.create_calliope(
            current_date, last_service_date, current_mileage, last_mileage)

        self.assertTrue(car.needs_service())

    def test_car_is_glissade(self):
        current_date = datetime.now()
        last_service_date = parser.parse("January 1, 2020 8:00 AM")
        current_mileage = 60000
        last_mileage = 0
        car = CarFactory.create_calliope(
            current_date, last_service_date, current_mileage, last_mileage)

        self.assertTrue(car.needs_service())

    def test_car_is_palindrome(self):
        current_date = datetime.now()
        last_service_date = parser.parse("January 1, 2020 8:00 AM")
        warning_light = True

        car = CarFactory.create_palindrome(
            current_date, last_service_date, warning_light)

        self.assertTrue(car.needs_service())

    def test_car_is_rorschach(self):
        current_date = datetime.now()
        last_service_date = parser.parse("January 1, 2017 8:00 AM")
        current_mileage = 60000
        last_mileage = 0
        car = CarFactory.create_rorschach(
            current_date, last_service_date, current_mileage, last_mileage)

        self.assertTrue(car.needs_service())

    def test_car_is_thovex(self):
        current_date = datetime.now()
        last_service_date = parser.parse("January 1, 2017 8:00 AM")
        current_mileage = 35000
        last_mileage = 0
        car = CarFactory.create_rorschach(
            current_date, last_service_date, current_mileage, last_mileage)

        self.assertTrue(car.needs_service())
