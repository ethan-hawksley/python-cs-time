def test_file(name: str):
    from os import path

    if path.exists(name):
        return False
    else:
        return True


def validate(number: str):
    try:
        number = float(number)
        return True
    except ValueError:
        return False


file_name = input("enter a name\n")
print(test_file(file_name))
# value = input("enter number\n")
# print(validate(value))
