
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime as dt
import datetime
from dateutil import parser
import unittest


class TestNubbin(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        last_service = 4.5
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)

        battery = NubbinBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        last_service = 3
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)

        battery = NubbinBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        last_service = 3.5
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)

        battery = SpindlerBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        last_service = 2.5
        current_date = dt.now()
        last_service_date = current_date - \
            datetime.timedelta(days=365 * last_service)

        battery = SpindlerBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())
