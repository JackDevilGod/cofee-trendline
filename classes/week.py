from classes.day import Day


class Week:
    def __init__(self) -> None:
        self.weekdays = [Day() for _ in range(7)]

    def set_value(self, time: list[int], value: int) -> None:
        self.weekdays[time[0] - 1].set_value(time[1:], value)

    def get_array(self) -> list:
        week = []

        for d in self.weekdays:
            week += d.get_array()

        return week
