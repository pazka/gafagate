
# [Yar,Month]
from datetime import date
type DataDate = date
type DataPoint = tuple[DataDate, float]


class DataHelper():
    def __init__(self, data):
        self.data: list[DataPoint] = data
        self.min_date: date = None
        self.max_date: date = None
        self.min_value: float = None
        self.max_value: float = None

        self.data.sort(key=lambda x: x[0])
        self.min_date = self.data[0][0]
        self.max_date = self.data[-1][0]

        self.min_value = min([x[1] for x in self.data])
        self.max_value = max([x[1] for x in self.data])

        self.filter_dates(date(2019, 1, 1), date(2023, 12, 31))

    def __getitem__(self, index: int) -> DataPoint:
        return self.data[index]

    def __iter__(self):
        return iter(self.data)

    def to_uv(self, data_point: DataPoint) -> float | None:
        return (data_point[1] - self.min_value) / (self.max_value - self.min_value)

    def get_value(self, date: DataDate) -> float | None:
        for i in range(len(self.data)):
            if self.data[i][0] == date:
                return self.data[i][1]
        return None

    def filter_dates(self, start: DataDate, end: DataDate) -> None:
        self.data = [x for x in self.data if x[0] >= start and x[0] <= end]
        self.min_date = self.data[0][0]
        self.max_date = self.data[-1][0]

    def clamp_values(self, min_value: float, max_value: float) -> None:
        self.data = [(x[0], min(max(x[1], min_value), max_value))
                     for x in self.data]
        self.min_value = min([x[1] for x in self.data])
        self.max_value = max([x[1] for x in self.data])
