def main():
    res = 0
    with open('input.txt') as f:
        lines = f.readlines()
    
    hands = {}

    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        hands[hand] = bid
    
    hands = {k: v for k, v in sorted(hands.items(), key=lambda item: (get_relative_hand_power(item[0]), get_value(item[0])))}

    for index, hand in enumerate(hands):
        hands[hand] = (index + 1) * hands[hand]

    print(sum(hands.values()))


def get_hand_power(hand):
    if five_of_a_kind(hand):
        return 6
    if four_of_a_kind(hand):
        return 5
    if full_house(hand):
        return 4
    if three_of_a_kind(hand):
        return 3
    if two_pair(hand):
        return 2
    if one_pair(hand):
        return 1
    return 0


def get_relative_hand_power(hand):
    if "J" not in hand:
        return get_hand_power(hand)
    
    max_power = get_hand_power(hand)
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for card in cards:
        max_power = max(max_power, get_hand_power(hand.replace("J", card)))
    
    return max_power


def one_pair(hand):
    sorted_hand = sorted(hand)
    for card in sorted_hand:
        if sorted_hand.count(card) == 2:
            return True
    return False

def two_pair(hand):
    sorted_hand = sorted(hand)
    pairs = 0
    for card in sorted_hand:
        if sorted_hand.count(card) == 2:
            pairs += 1
    return pairs == 2 * 2

def three_of_a_kind(hand):
    sorted_hand = sorted(hand)
    for card in sorted_hand:
        if sorted_hand.count(card) == 3:
            return True
    return False

def full_house(hand):
    return one_pair(hand) and three_of_a_kind(hand)

def four_of_a_kind(hand):
    sorted_hand = sorted(hand)
    for card in sorted_hand:
        if sorted_hand.count(card) == 4:
            return True
    return False

def five_of_a_kind(hand):
    return len(set(hand)) == 1


def get_value(hand):
    hand = hand.replace('A', 'Z')
    hand = hand.replace('K', 'Y')
    hand = hand.replace('Q', 'X')
    hand = hand.replace('T', 'V')
    hand = hand.replace('J', '1')
    return hand


if __name__ == '__main__':
    main()
