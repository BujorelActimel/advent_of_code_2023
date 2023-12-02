def main():
    sum = 0
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            calibration_value = get_first_digit(line) + get_last_digit(line)
            # print(calibration_value)
            sum += int(calibration_value)

    print(sum)


def get_first_digit(line):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for digit, value in digits.items():
            if line[i:i+len(digit)] == digit:
                return str(value)
    return None

def get_last_digit(line):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return line[i]
        for digit, value in digits.items():
            if line[i-len(digit)+1:i+1] == digit:
                return str(value)
    return None


# def get_first_digit(line):
#     digits = {
#         "one": 1,
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eight": 8,
#         "nine": 9,
#     }
#     first_digit = [None, -1]
#     for digit in digits:
#         if digit in line and first_digit[1] == -1:
#             first_digit = [digits[digit], line.index(digit)]

#         elif digit in line and line.index(digit) < first_digit[1]:
#             first_digit = [digits[digit], line.index(digit)]

#     for char in line:
#         if char.isdigit() and first_digit[1] == -1:
#             first_digit = [int(char), line.index(char)]
#         if char.isdigit() and line.index(char) < first_digit[1]:
#             first_digit = [int(char), line.index(char)]

#     return str(first_digit[0])



# def get_last_digit(line):
#     digits = {
#         "one": 1,
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eight": 8,
#         "nine": 9,
#     }
#     last_digit = [None, -1]
#     for digit in digits:
#         if digit in line and last_digit[1] == -1:
#             last_digit = [digits[digit], line.index(digit)]

#         elif digit in line and line.index(digit) > last_digit[1]:
#             last_digit = [digits[digit], line.index(digit)]

#     for char in line:
#         if char.isdigit() and last_digit[1] == -1:
#             last_digit = [int(char), line.index(char)]
#         if char.isdigit() and line.index(char) > last_digit[1]:
#             last_digit = [int(char), line.index(char)]

#     return str(last_digit[0])


if __name__ == '__main__':
    main()
