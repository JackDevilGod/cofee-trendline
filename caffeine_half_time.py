def caffeine_half_time(time: int, value: float) -> float:
    half_time = 300
    exp = time/half_time
    mult = (0.5)**exp

    return value * mult
