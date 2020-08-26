from dataclasses import dataclass


@dataclass
class MonthDelta:

    months: int

    def __add__(self, other):
        if isinstance(other, Month):
            months = other.year * 12 + other.month + self.months
            year, month = divmod(months-1, 12)
            return Month(year, month+1)
        if isinstance(other, MonthDelta):
            return MonthDelta(self.months + other.months)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, MonthDelta):
            return MonthDelta(self.months - other.months)
        return NotImplemented


@dataclass
class Month:

    year: int
    month: int

    def __sub__(self, other):
        if isinstance(other, Month):
            return MonthDelta(self.year*12+self.month - (other.year*12+other.month))
        elif isinstance(other, MonthDelta):
            months = self.year * 12 + self.month - other.months
            year, month = divmod(months-1, 12)
            return Month(year, month+1)
        return NotImplemented


x = Month(2000, 4) - MonthDelta(5)
print(x.year, " ", x.month)
