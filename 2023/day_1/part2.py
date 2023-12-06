# Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven,
# eight, and nine also count as valid "digits".


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


total = 0
line_num = 1
for line in open("input2.txt"):
    line = insert_text_digits(line)
    digits = [ch for ch in line if ch.isdigit()]
    
    line_total = int(digits[0] + digits[-1])
    print(f"{line_num}: {digits} = {line_total}")
    
    total += line_total
    line_num += 1

print(total)
