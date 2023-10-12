#!/usr/bin/env python3
# spindler_battery.py

from battery.battery import AbstractBattery
from datetime import datetime
from dateutil.relativedelta import relativedelta


class SpindlerBattery(AbstractBattery):

    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date: datetime = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        time_elapsed = relativedelta(self.current_date, self.last_service_date)

        return time_elapsed.years >= 3
