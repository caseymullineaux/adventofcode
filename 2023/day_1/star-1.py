# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.

with open("2023/day_1/input_part_1.txt", "r") as f:
    lines = f.readlines()

numbers = []

for line in lines:
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            else:
                last_digit = char
    if last_digit is None:
        last_digit = first_digit
    number = int(first_digit + last_digit)
    numbers.append(number)

total = sum(numbers)
print(total)