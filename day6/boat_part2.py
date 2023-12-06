def main():
    with open("input.txt") as f:
        lines = f.readlines()
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    
    time = int("".join(times))
    distance = int("".join(distances))

    print(get_winning_posibilities(time, distance))


def get_winning_posibilities(time, distance):
    posibilities = 0
    for hold_time in range(time + 1):
        time_left = time - hold_time
        current_distance = hold_time * time_left
        if current_distance > distance:
            posibilities += 1
    return posibilities


if __name__ == "__main__":
    main()
