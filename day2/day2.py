def data():
    games = []
    with open("data.txt", "r") as file:
        for line in file.readlines():
            aline = line.strip("\n").split(": ")
            gameId = int(aline[0].split(" ")[1])
            hands = []
            for h in aline[1].split("; "):
                hand = [0, 0, 0]
                for d in h.split(", "):
                    value = d.split(" ")
                    if value[1] == "red":
                        hand[0] += int(value[0])
                    if value[1] == "green":
                        hand[1] += int(value[0])
                    if value[1] == "blue":
                        hand[2] += int(value[0])

                hands.append(hand)
            games.append((gameId, hands))
    return games


def compareHand(hand):
    return all(map(lambda i, j: i <= j, hand, [12, 13, 14]))


def add():
    games = data()
    sumId = 0
    for gameId, hands in games:
        res = [compareHand(h) for h in hands]
        if sum(res) == len(res):
            sumId += gameId
    return sumId


def main():
    print(add())


if __name__ == "__main__":
    main()
