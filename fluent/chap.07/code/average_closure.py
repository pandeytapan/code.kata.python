def make_averager():
    series = []

    def averager(value):
        series.append(value)
        return sum(series) / len(series)

    return averager
