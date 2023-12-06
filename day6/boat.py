def main():
    ans = 1
    with open("input.txt") as f:
        lines = f.readlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
        
    for i in range(len(times)):
        ans *= get_winning_posibilities(times[i], distances[i])
    
    print(ans)


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
