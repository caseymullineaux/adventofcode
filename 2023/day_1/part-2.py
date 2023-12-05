# Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven,
# eight, and nine also count as valid "digits".

with open("2023/day_1/input2.txt", "r") as f:
    lines = f.readlines()


def insert_text_digits(line):
    text_digit = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]
    for text, digit in text_digit:
        line = line.replace(text, f"{text}{digit}")
    return line


numbers = []
for line in lines:
    first_digit = None
    last_digit = None

    line = insert_text_digits(line)
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            else:
                last_digit = char
    if last_digit is None:
        last_digit = first_digit
    number = int(first_digit + last_digit)
    print(f"{line}: {number}")
    numbers.append(number)

total = sum(numbers)
print(f"total: {total}")
