def password_generator(word):
    vowels = ("a", "e", "i", "o", "u")
    password = ""
    for i in range(len(word)):
        if word[i] in vowels:
            password += str(i)
    return password


def odd_parity(number: str):
    odds = 0
    for i in number:
        if i == "1":
            odds += 1
            # count the number of 1 in the sequence
    if odds % 2 == 1:
        return True
        # successful if there is an odd amount of 1
    else:
        return False


if __name__ == "__main__":
    print(password_generator("kapow") + password_generator("password"))
    print(odd_parity("111000111"))
