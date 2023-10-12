
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime
from dateutil import parser
import unittest


class TestNubbin(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        last_service_date = parser.parse("January 1, 2016 8:00 AM")
        current_date = datetime.now()

        battery = NubbinBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        last_service_date = parser.parse("December 25, 2020 8:00 PM")
        current_date = datetime.now()

        battery = NubbinBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        last_service_date = parser.parse("January 1, 2020 10:00 AM")
        current_date = datetime.now()

        battery = SpindlerBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        last_service_date = parser.parse("December 25, 2022 1:00 PM")
        current_date = datetime.now()

        battery = SpindlerBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())
