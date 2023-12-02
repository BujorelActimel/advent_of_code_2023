def main():
    res = 0
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            # print(power(line))
            res += power(line)
    print(res)


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def power(line):
    line = line.split(": ")[1]
    sets = line.split("; ")
    minimum = {"red": None, "green": None, "blue": None}
    for s in sets:
        cubes = s.split(", ")
        for c in cubes:
            color = c.split(" ")[1]
            ammount = int(c.split(" ")[0])
            if(minimum[color] == None or ammount > minimum[color]):
                minimum[color] = ammount
    return minimum["red"] * minimum["green"] * minimum["blue"]


if __name__ == '__main__':
    main()
