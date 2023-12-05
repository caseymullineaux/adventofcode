# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.

total = 0
for line in open("2023/day_1/input1.txt"):
    digits = [ch for ch in line if ch.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)
