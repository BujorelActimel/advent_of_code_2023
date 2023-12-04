def main():
    number_of_cards = 0
    cards = {}
    with open("input.txt") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            cards[i + 1] = 1

        for line in lines:
            score = get_score(line)
            for i in range(lines.index(line) + 1, lines.index(line) + 1 + score):
                for _ in range(cards[lines.index(line) + 1]):
                    cards[i + 1] += 1
    
    for card in cards:
        number_of_cards += cards[card]

    print(number_of_cards)


def get_score(line):
    score = 0
    line = line.split(": ")[1]
    winning_numbers, numbers = line.split(" | ")
    winning_numbers = winning_numbers.split()
    numbers = numbers.split()
    
    for number in numbers:
        if number in winning_numbers:
            score += 1
    
    return score

if __name__ == '__main__':
    main()
