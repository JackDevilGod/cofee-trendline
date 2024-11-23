import matplotlib.pyplot as plt


def plot_week(week: list[float, int]) -> None:
    x = [num for num in range(1, len(week) + 1)]

    day_minutes = (24 * 60)

    v_lines = [0, day_minutes, day_minutes * 2, day_minutes * 3, day_minutes * 4, day_minutes * 5,
               day_minutes * 6, len(x) - 1]

    v_lines_min = [0 for _ in range(len(v_lines))]
    v_lines_max = [max(week) for _ in range(len(v_lines))]

    plt.vlines(v_lines, v_lines_min, v_lines_max, colors=(1, 0, 0))

    plt.plot(x, week)
    plt.show()