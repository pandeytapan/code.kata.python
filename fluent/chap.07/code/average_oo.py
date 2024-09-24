class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, value):
        self.series.append(value)
        return sum(self.series)/len(self.series)
