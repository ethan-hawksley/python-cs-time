def division_check(num1, num2):
    if num2 == 0:
        return False
    elif num1 % num2 == 0:
        return True
    else:
        return False


def charging_cost(time):
    from math import floor

    if time < 15:
        time = 15
    cost = "£" + str(time * 0.2 + 1)
    points = floor(time * 1.5)
    return (cost, points)


if __name__ == "__main__":
    print(division_check(1, 8))
    print(charging_cost(12))
