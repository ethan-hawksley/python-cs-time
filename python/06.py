def happy_number_checker(number: int):
    while number != 4:
        new_number = 0
        # iterate over all digits in the number
        for i in str(number):
            new_number += int(i) ** 2
        number = new_number
        # the number is 1 so it is happy
        if number == 1:
            return True
    # the number was 4 so it is never happy
    return False


def predator_sim(prey: int, predators: int, a: float, b: float, c: float, d: float):
    generations = [(prey, predators)]
    e = 2.718  # the exponential constant
    while prey >= 2 and predators >= 2:
        # formulas of growth
        prey_growth_rate = e ** (a - (c * predators))
        next_prey = prey * prey_growth_rate
        predator_growth_rate = e ** ((d * c * (next_prey - prey) - b))
        next_predators = predators * predator_growth_rate

        prey = round(next_prey)
        predators = round(next_predators)
        generations.append((prey, predators))  # add to the record
    return generations


if __name__ == "__main__":
    print(happy_number_checker(47))
    print(predator_sim(50, 8, 0.8, 0.5, 0.1, 0.3))
