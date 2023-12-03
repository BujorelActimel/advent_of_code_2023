def main():
    total_sum = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            total_sum = check(i, lines, total_sum)
        
    print(total_sum)


def check(i, lines, total_sum):
    j = 0
    while j < len(lines[0]):
        num = ""
        starting_point = j
        while j < len(lines[i]) and lines[i][j].isdigit():
            num += lines[i][j]
            j += 1
        ending_point = j

        if num != "":
            if exist_adjacent_symbols(starting_point, ending_point, i, lines):
                print(num)
                total_sum += int(num)
        else:
            j += 1
    
    return total_sum


def exist_adjacent_symbols(starting_point, ending_point, i, lines):
    k = starting_point - 1
    while k < ending_point + 1:
        if i - 1 >= 0:
            if 0 <= k < len(lines) and isSymbol(lines[i - 1][k]):
                print(lines[i - 1][k])
                return True
        if i + 1 < len(lines):
            if 0 <= k < len(lines) and isSymbol(lines[i + 1][k]):
                print(lines[i + 1][k])
                return True
        k += 1
    
    if starting_point - 1 >= 0 and isSymbol(lines[i][starting_point - 1]):
        print(lines[i][starting_point - 1])
        return True
    if ending_point< len(lines) and isSymbol(lines[i][ending_point]):
        print(lines[i][ending_point])
        return True

    return False


def isSymbol(char):
    return not char.isdigit() and char.isascii() and char not in " \n."


if __name__ == '__main__':
    main()
