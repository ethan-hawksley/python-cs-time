def rock_paper_scissors():
    from random import randint

    CHOICES = ["rock", "paper", "scissors"]

    # dictionary for looking up what beats what
    WINNING_COMBINATIONS = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    player_score = 0
    computer_score = 0

    while player_score < 10 and computer_score < 10:
        choice = ""
        # ask until valid answer is given
        while choice not in CHOICES:
            choice = input("choose your choice\n")

        computer_choice = CHOICES[randint(0, 2)]

        if computer_choice == choice:
            print("you draw")
        elif WINNING_COMBINATIONS[computer_choice] == choice:
            computer_score += 1
            print("you lose")

        else:
            # the only possible scenario left is winning
            player_score += 1
            print("you win")

        # print the choices
        print(f"your choice was {choice} and their choice was {computer_choice}")
        print(
            f"the points are now computer at {computer_score} and player at {player_score}"
        )


def password_verifier():
    password = ""
    valid = False
    NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while not valid:
        password = input("enter password\n")
        valid = True
        if len(password) < 8:
            print("too short")
            valid = False
        if password.lower() == password:
            # password is all lowercase
            print("need capital")
            valid = False
        if password.upper() == password:
            # password is all uppercase
            print("need lowercase")
            valid = False
        contain_number = False
        for letter in password:
            # iterate over all letters and check if they are a number
            if letter in NUMBERS:
                contain_number = True
        if not contain_number:
            print("need number")
            valid = False

    print("valid password")
    return password


if __name__ == "__main__":
    # rock_paper_scissors()
    print("your password is " + password_verifier())
