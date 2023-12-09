def main():
    res = 0
    with open('input.txt') as f:
        lines = f.readlines()
    
    histories = []

    for line in lines:
        numbers = [int(x) for x in line.split()]
        histories.append(numbers)

    for history in histories:
        res += get_prediction(history)

    print(res)


def get_prediction(history):
    cpy = history.copy()
    diferences = []
    while not all_zeroes(history):
        diference = []
        for i in range(1, len(history)):
            diference.append(history[i] - history[i-1])
        
        diferences.append(diference)
        history = diference

    prediction = 0

    for i in range(len(diferences) - 1, -1, -1):
        prediction = diferences[i][-1] + prediction

    return cpy[-1] + prediction


def all_zeroes(history):
    for number in history:
        if number != 0:
            return False
    return True


if __name__ == '__main__':
    main()
