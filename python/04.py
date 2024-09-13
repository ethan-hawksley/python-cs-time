def name_separator(name):
    space = name.find(" ")
    first_name = name[0:space]
    surname = name[space + 1 :]
    return (first_name, surname)


def function_namer(part1, part2, format):
    if format == "kebab-case":
        return part1.lower() + "-" + part2.lower()
    elif format == "snake_case":
        return part1.lower() + "_" + part2.lower()
    elif format == "camelCase":
        return part1.lower() + part2.title()
    elif format == "PascalCase":
        return part1.title() + part2.title()
    else:
        return "failure"


if __name__ == "__main__":
    print(name_separator("Bob Charles"))
    print(function_namer("super", "Important", "snake_case"))
