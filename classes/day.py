from classes.hour import Hour


class Day:
    def __init__(self) -> None:
        self.time_scale = [Hour() for _ in range(24)]

    def set_value(self, time: list[int], value: int) -> None:
        self.time_scale[time[0] - 1].set_value(time[-1], value)

    def get_array(self) -> list:
        day = []

        for h in self.time_scale:
            day += h.get_array()

        return day
