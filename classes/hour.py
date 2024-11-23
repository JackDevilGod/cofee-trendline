from classes.minute import Minute


class Hour:
    def __init__(self) -> None:
        self.time_scale = [Minute() for _ in range(60)]

    def set_value(self, time: int, value: int) -> None:
        self.time_scale[time - 1].value = value

    def get_array(self) -> list:
        return [m.value for m in self.time_scale]
