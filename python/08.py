def maths_test():
    from random import randint

    questions_answers = [["", 0], ["", 0], ["", 0], ["", 0], ["", 0]]
    for i in questions_answers:
        num1 = randint(10, 100)
        num2 = randint(10, 100)
        i[0] = str(num1) + " + " + str(num2)
        i[1] = num1 + num2

    carry_on = True
    while carry_on:
        name = input("enter name\n")
        score = 0
        for i in questions_answers:
            if int(input("what is the answer to " + str(i[0]) + "\n")) == i[1]:
                score += 1
                print("correct")
        print(f"{name} got {score}")
        carry_on = input("continue? (True, False)")
        if carry_on.lower() == "false":
            carry_on = False


def strong_checker():
    from math import factorial

    number = input("enter number\n")
    total = 0
    for letter in number:
        total += factorial(int(letter))
    if total == int(number):
        print("strong")
    else:
        print("weak")


if __name__ == "__main__":
    strong_checker()
    # maths_test()
