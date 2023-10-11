#!/usr/bin/env python3
# sternman_engine.py

from engine.engine import AbstractEngine
from datetime import datetime


class SternmanEngine(AbstractEngine):

    last_service_date: datetime
    warning_light_is_on: bool

    def __init__(self, last_service_date: datetime, warning_light_is_on: bool):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def set_warning_light(self):
        self.warning_light_is_on = False

    def needs_service(self) -> bool:
        return self.warning_light_is_on
