def amino_acid():
    f = open("python/data/amino_acid.txt")
    dna = f.readline().strip()
    sequence = input("what acid to check\n")
    if len(dna) % 3 == 0:
        count = 0
        for i in range(len(dna) // 3):
            if dna[3 * i : 3 * i + 3] == sequence:
                count += 1
        print(count)


def shopping_list():
    import os

    list_path = "python/data/" + input("name of list: ") + ".txt"
    if not (os.path.exists(list_path)):
        file_list = open(list_path, "x")  # create file
        file_list.close()
    file_list = open(list_path, "r")  # open file to read existing list

    items = [""]
    _ = items.pop(0)  # prevent ide complaints so it knows the type
    for line in file_list:
        items.append(line.strip())  # read file
    file_list.close()
    file_list = open(list_path, "w")

    looping = True
    while looping:
        match input("v to view, a to add, r to remove, s to stop: "):
            case "v":
                print(items)
            case "a":
                items.append(
                    input("what to add: ")
                )  # \n so newlines are inserted when calling writelines
            case "r":
                items.remove(input("what to remove: "))
            case "s":
                looping = False  # stop
            case _:
                print("not option")
    for i in items:
        _ = file_list.write(i)
        _ = file_list.write("\n")
    file_list.close()


if __name__ == "__main__":
    amino_acid()
    shopping_list()
