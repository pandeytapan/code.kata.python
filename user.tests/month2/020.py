class MonthDelta:

    def __init__(self, months):
        self.months = months

    def __eq__(self, other):
        if isinstance(other, MonthDelta):
            return self.months == other.months
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Month):
            months = other.year * 12 + other.month + self.months
            year, month = divmod(months-1, 12)
            return Month(year, month+1)
        return NotImplemented

    __radd__ = __add__

    def __rsub__(self, other):
        if isinstance(other, Month):
            months = other.year * 12 + other.month - self.months
            year, month = divmod(months-1, 12)
            return Month(year, month+1)
        return NotImplemented


class Month:

    def __init__(self, year, month):
        self.year, self.month = year, month

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Month):
            return MonthDelta(self.year*12+self.month - (other.year*12+other.month))
        return NotImplemented


x = Month(2000, 4) - MonthDelta(5)
print(x.year, " ", x.month)
