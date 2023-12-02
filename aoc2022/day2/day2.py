def games():
    lines = open("data.txt", "r")
    return lines.read()


def part1():
    """
    'A X' = 1 = rock
    'B Y' = 2 = paper
    'C Z' = 3 = scissors
    """
    points = 0
    data = games().split("\n")
    for i in data:
        if i == "A X":
            points += 4
        if i == "B X":
            points += 1
        if i == "C X":
            points += 7

        if i == "A Y":
            points += 8
        if i == "B Y":
            points += 5
        if i == "C Y":
            points += 2

        if i == "A Z":
            points += 3
        if i == "B Z":
            points += 9
        if i == "C Z":
            points += 6

    return points


def part2():
    """
    'A X' = 1 = rock
    'B Y' = 2 = paper
    'C Z' = 3 = scissors
    """
    points = 0
    data = games().split("\n")
    for i in data:
        if i == "A X":
            points += 3
        if i == "B X":
            points += 1
        if i == "C X":
            points += 2

        if i == "A Y":
            points += 4
        if i == "B Y":
            points += 5
        if i == "C Y":
            points += 6

        if i == "A Z":
            points += 8
        if i == "B Z":
            points += 9
        if i == "C Z":
            points += 7

    return points


def main():
    print(part1())
    print(part2())



if __name__ == "__main__":
    main()
