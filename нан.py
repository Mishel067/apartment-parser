from datetime import timedelta as td
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today, weekday, considering_day=False):
        self.today = today
        self.weekday = weekday
        self.is_considering_day = considering_day

    def date(self):
        days = abs(self.today.isoweekday() - self.weekday.value + 1)
        if not self.is_considering_day and days == 0:
            days = 7
        return self.today + td(days=days)

    def days_until(self):
        days = abs(self.today.isoweekday() - self.weekday.value + 1)
        if not self.is_considering_day and days == 0:
            days = 7
        return days







