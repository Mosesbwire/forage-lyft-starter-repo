#!/usr/bin/env python3

# engine.py
""" Abstract class for the engine """

from abc import ABC, abstractmethod


class AbstractEngine(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass
