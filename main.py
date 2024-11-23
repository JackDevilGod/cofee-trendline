from classes.week import Week
from functions.formulas import caffeine_half_time
from functions.apply_formula import apply_formula
from functions.plot_week import plot_week


def main():
    w = Week()

    # syntax [day, hour, minute]
    w.set_value([1, 8, 0], 120)
    w.set_value([3, 10, 0], 120)
    w.set_value([4, 8, 0], 120)

    y = apply_formula(w, caffeine_half_time)

    plot_week(y)


if __name__ == '__main__':
    main()
