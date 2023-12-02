def data():
    lines = open("data.txt", "r")
    return lines.read()


def elfs():
    total_cals = []
    cals = data().strip().split("\n\n")
    for i, block in enumerate(cals, start=1):
        numbers = [int(num) for num in block.split('\n')]
        total_sum = sum(numbers)
        total_cals.append(total_sum)
    total_cals.sort()
    first = total_cals[-1]
    second = total_cals[-2]
    third = total_cals[-3]
    total = first + second + third
    return total


def main():
    print(elfs())


if __name__ == "__main__":
    main()
