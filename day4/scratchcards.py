def main():
    with open("input.txt") as f:
        lines = f.readlines()
        score = 0
        for line in lines:
            score += get_score(line)
    print(score)


def get_score(line):
    score = 0
    line = line.split(": ")[1]
    winning_numbers, numbers = line.split(" | ")
    winning_numbers = winning_numbers.split()
    numbers = numbers.split()
    
    for number in numbers:
        if number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
    
    return score


if __name__ == '__main__':
    main()
