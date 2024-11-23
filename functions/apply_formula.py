from classes import week
from typing import Callable


def apply_formula(time_scale: week, formula: Callable[[float], float]) -> list[float]:
    week_array = time_scale.get_array()

    for index, value in enumerate(week_array):
        if value != 0:
            first_drink = index

    if first_drink + 1 >= len(week_array):
        current_index = 0
    else:
        current_index = first_drink + 1

    while True:
        print(current_index)
        if current_index - 1 >= 0:
            week_array[current_index] = (week_array[current_index] +
                                         formula(week_array[current_index - 1]))
        else:
            week_array[current_index] = week_array[current_index] + formula(week_array[-1])

        if current_index + 1 >= len(week_array):
            current_index = 0
        else:
            current_index = current_index + 1

        if current_index == first_drink:
            break

    return week_array
