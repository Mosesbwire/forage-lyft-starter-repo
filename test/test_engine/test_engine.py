

from datetime import datetime
from dateutil import parser
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
import unittest


class TestCapulet(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30000

        last_service_mileage_a = 70000
        current_mileage_a = 105000

        engine_one = CapuletEngine(last_service_mileage, current_mileage)
        engine_two = CapuletEngine(last_service_mileage_a, current_mileage_a)

        self.assertTrue(engine_one.needs_service())
        self.assertTrue(engine_two.needs_service())

    def test_engine_does_not_need_service(self):
        last_service_mileage = 30000
        current_mileage = 59999

        last_service_mileage_a = 60000
        current_mileage_b = 85000

        engine = CapuletEngine(last_service_mileage, current_mileage)
        engine_a = CapuletEngine(last_service_mileage_a, current_mileage_b)


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60000

        last_service_mileage_a = 70000
        current_mileage_a = 135000

        engine_one = WilloughbyEngine(last_service_mileage, current_mileage)
        engine_two = WilloughbyEngine(
            last_service_mileage_a, current_mileage_a)

        self.assertTrue(engine_one.needs_service())
        self.assertTrue(engine_two.needs_service())

    def test_engine_does_not_need_service(self):
        last_service_mileage = 60000
        current_mileage = 119999

        last_service_mileage_a = 60000
        current_mileage_b = 115000

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        engine_a = WilloughbyEngine(last_service_mileage_a, current_mileage_b)

        self.assertFalse(engine.needs_service())
        self.assertFalse(engine_a.needs_service())


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light = True
        last_service_date = parser.parse("January 15, 2015 8:00 AM")

        engine = SternmanEngine(last_service_date, warning_light)

        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        warning_light = False
        last_service_date = parser.parse("January 15, 2015 8:00 AM")

        engine = SternmanEngine(last_service_date, warning_light)

        self.assertFalse(engine.needs_service())
