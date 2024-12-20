class Minute:
    def __init__(self) -> None:
        self._value: int = 0

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = value
