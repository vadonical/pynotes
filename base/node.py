from enum import Enum


class DateMode(Enum):
    DEFAULT = 0
    LUNAR = 1


class Date:
    def __init__(self, year: int, month: int, day: int, mode: DateMode = DateMode.DEFAULT):
        pass

    def __add__(self, other):
        print(other)

    def converse(self):
        pass

    def get_today(self, ):
        pass

