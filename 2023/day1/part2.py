# Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven,
# eight, and nine also count as valid "digits".
import re

def find_text_digits(line):
    """
    Find the position of the text digits in the line.
    """
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
    text_pos = []

    for text, digit in text_digit:
        for match in re.finditer(text, line):
            text_pos.append((match.start(), digit))

    return text_pos.sort()


total = 0
line_num = 1
for line in open("day1/test.txt"):
    text_pos = find_text_digits(line)

    # find the position of the digits
    digit_pos = []
    [digit_pos.append((i, char)) for i, char in enumerate(line) if char.isdigit()]
    
    # merge the two lists
    if text_pos:
        digit_pos.extend(text_pos)
    digit_pos.sort()

    # concatenate the first and last digits
    line_total = int(digit_pos[0][1] + digit_pos[-1][1])
    print(f"{line_num}: {digit_pos} = {line_total}")
    
    # sum the total
    total += line_total
    line_num += 1

print(total)
