def main():
    res = 0
    # Game 1: 2 red, 2 green; 6 red, 3 green; 2 red, 1 green, 2 blue; 1 red
    total_cubes = {"red": 12, "green": 13, "blue": 14}

    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            if(possible(line, total_cubes)):
                res += get_game_index(line)
    
    print(res)


def possible(line, total_cubes):
    line = line.split(": ")[1]
    sets = line.split("; ")
    for s in sets:
        copy_cubes = total_cubes.copy()
        cubes = s.split(", ")
        for c in cubes:
            color = c.split(" ")[1]
            ammount = int(c.split(" ")[0])
            if(copy_cubes[color] < ammount):
                return False
            else:
                copy_cubes[color] -= ammount
    return True

        

def get_game_index(line):
    line = line.split(": ")[0]
    return int(line[5:])


if __name__ == '__main__':
    main()