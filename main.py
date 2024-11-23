import matplotlib.pyplot

from classes.week import Week
from caffeine_half_time import caffeine_half_time


def main():
    w = Week()

    w.set_value([1, 8, 0], 120)
    w.set_value([3, 10, 0], 120)
    w.set_value([4, 8, 0], 120)

    week_array = w.get_array()

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
            week_array[current_index] = week_array[current_index] + caffeine_half_time(1, week_array[current_index - 1])
        else:
            week_array[current_index] = week_array[current_index] + caffeine_half_time(1, week_array[-1])

        if current_index + 1 >= len(week_array):
            current_index = 0
        else:
            current_index = current_index + 1

        if current_index == first_drink:
            break

    x = [num for num in range((1 * 7 * 24 * 60))]

    day_minutes = (24 * 60)
    v_lines = [0, day_minutes, day_minutes * 2, day_minutes * 3, day_minutes * 4, day_minutes * 5, len(x) - 1]
    v_lines_min = [0 for _ in range(len(v_lines))]
    v_lines_max = [120 for _ in range(len(v_lines))]

    matplotlib.pyplot.vlines(v_lines, v_lines_min, v_lines_max, colors=(1, 0, 0))

    matplotlib.pyplot.plot(x, week_array)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
