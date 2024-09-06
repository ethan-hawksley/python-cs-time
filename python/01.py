def EnergyUsage(previous, current, calorific_value):
    return (current - previous) * 1.022 * (calorific_value / 3.6) * 2.84


def CircleProperties(diameter, arc_angle):
    return [
        diameter / 2,
        ((diameter / 2) ** 2) * 3.14,
        diameter * 3.14,
        diameter * 3.14 * arc_angle / 360,
    ]


if __name__ == "__main__":
    print(EnergyUsage(10, 11, 39.3))
    print(CircleProperties(20, 90))
