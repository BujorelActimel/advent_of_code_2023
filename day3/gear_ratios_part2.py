class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Num:
    def __init__(self, value, start_position, end_position):
        self.value = value
        self.start_position = start_position
        self.end_position = end_position

    def __str__(self):
        return "Num: " + str(self.value) + " Start: " + str(self.start_position.x) + ", " + str(self.start_position.y) + " End: " + str(self.end_position.x) + ", " + str(self.end_position.y) + "\n"

    def __repr__(self):
        return str(self)


class Symbol:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position

    def __str__(self):
        return "Symbol: " + str(self.symbol) + " Position: " + str(self.position.x) + ", " + str(self.position.y) + "\n"

    def __repr__(self):
        return str(self)


def main():
    res = 0
    with open("input.txt") as f:
        lines = f.readlines()
        nums = parse_num(lines)
        # print(nums)
        stars = parse_stars(lines)
        # print(stars)

        for star in stars:
            prod = 1
            nums_in_prod = 0
            for num in nums:
                if adjacent(num, star):
                    prod *= num.value
                    nums_in_prod += 1

            if nums_in_prod == 2:
                res += prod

    print(res)

                    
def parse_num(lines):
    nums = []
    i = 0
    while i < len(lines):
        line = lines[i]
        j = 0
        while j < len(line):
            num  = ""
            start_j = j
            while line[j].isdigit():
                num += line[j]
                j += 1
            if num != "":
                nums.append(Num(int(num), Position(i, start_j), Position(i, j - 1)))
            j += 1
        i += 1
    return nums


def parse_stars(lines):
    stars = []
    i = 0
    while i < len(lines):
        line = lines[i]
        j = 0
        while j < len(line):
            if line[j] == "*":
                stars.append(Symbol("*", Position(i, j)))
            j += 1
        i += 1
    return stars


def adjacent(num, star):
    if num.start_position.x - 1 <= star.position.x <= num.end_position.x + 1:
        if num.start_position.y - 1 <= star.position.y <= num.end_position.y + 1:
            return True
    return False


if __name__ == '__main__':
    main()
