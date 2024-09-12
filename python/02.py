def Grade_Calculator(marks):
    boundaries = [
        [80, 9],
        [67, 8],
        [54, 7],
        [41, 6],
        [31, 5],
        [22, 4],
        [13, 3],
        [4, 2],
        [2, 1],
    ]
    for i in range(len(boundaries)):
        if marks >= boundaries[i][0]:
            grade = boundaries[i][1]
            if i != 0:
                next_grade = boundaries[i - 1][1]
                marks_away = boundaries[i - 1][0] - marks
                return f"Achieved grade {grade}, is {marks_away} marks away from a {next_grade}."
            else:
                return f"Achieved grade {grade}"


def Day_Format(day, format):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    short_days = {
        1: "Mon",
        2: "Tue",
        3: "Wed",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun",
    }
    char = {
        1: "M",
        2: "Tu",
        3: "W",
        4: "Th",
        5: "F",
        6: "Sa",
        7: "Su",
    }
    match format:
        case "day":
            return days[day]
        case "shortday":
            return short_days[day]
        case "char":
            return char[day]
    return "invalid"


if __name__ == "__main__":
    print(Grade_Calculator(70))
    print(Day_Format(3, "char"))
