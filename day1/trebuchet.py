def main():
    sum = 0
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            calibration_value = ""
            for char in line:
                if char.isdigit():
                    calibration_value += char

            if not len(calibration_value):
                continue

            if len(calibration_value) == 1:
                calibration_value += calibration_value[0]
            
            if len(calibration_value) > 2:
                calibration_value = calibration_value[0] + calibration_value[-1]
            
            sum += int(calibration_value)

    print(sum)


if __name__ == '__main__':
    main()
