def amino_acid():
    file = open("python/data/amino_acid.txt")
    dna = file.readline().strip()
    sequence = input("what acid to check\n")
    if len(dna) % 3 == 0:
        count = 0
        for i in range(len(dna) // 3):
            if dna[3 * i : 3 * i + 3] == sequence:
                count += 1
        print(count)


if __name__ == "__main__":
    amino_acid()
