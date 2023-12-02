import re


def data():
    lines = open("data.txt", "r")
    return lines.read()


def find():
    line = data().split()
    numbers = [int(''.join(re.findall(r'\d', item)[:1] + re.findall(r'\d', item)[-1:])) for item in line]
    return numbers


def add():
    my_numbers = find()
    total = sum(my_numbers)
    return total


def main():
    print(find())
    print(add())


if __name__ == "__main__":
    main()
