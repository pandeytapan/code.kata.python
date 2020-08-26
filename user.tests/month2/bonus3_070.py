from dataclasses import dataclass
from datetime import date


@dataclass(order=True, frozen=True)
class MonthDelta:

    __slots__ = ['months']

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

    def __mul__(self, other):
        if isinstance(other, int):
            return MonthDelta(self.months * other)
        return NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            return MonthDelta(self.months / other)
        if isinstance(other, MonthDelta):
            return self.months / other.months
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, int):
            return MonthDelta(self.months // other)
        if isinstance(other, MonthDelta):
            return self.months // other.months
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, int):
            return MonthDelta(self.months % other)
        if isinstance(other, MonthDelta):
            return self.months % other.months
        return NotImplemented

    def __neg__(self):
        return MonthDelta(-self.months)

    def __sub__(self, other):
        if isinstance(other, MonthDelta):
            return MonthDelta(self.months - other.months)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Month):
            months = other.year * 12 + other.month - self.months
            year, month = divmod(months-1, 12)
            return Month(year, month+1)
        return NotImplemented


@dataclass(order=True, frozen=True)
class Month:

    __slots__ = ['year', 'month']

    year: int
    month: int

    def __sub__(self, other):
        if isinstance(other, Month):
            return MonthDelta(self.year*12+self.month - (other.year*12+other.month))
        return NotImplemented

    def __format__(self, fmt):
        return date(self.year, self.month, 1).__format__(fmt)


x = Month(2000, 4) - MonthDelta(5)
print(x.year, " ", x.month)
