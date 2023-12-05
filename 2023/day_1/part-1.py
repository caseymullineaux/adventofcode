# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.

# open a text file for reading, and read each line into a list
with open("2023/day_1/input.txt", "r") as f:
    lines = f.readlines()

# locate the first position of a digit
# locate the last position of a digit
# combine the two digits to form a single two-digit number
# add the two-digit number to a list
# repeat for each line
# sum the list
# print the sum

# initialize a list to hold the two-digit numbers
numbers = []

# loop through each line in the list of lines
for line in lines:
    # initialize a variable to hold the first digit
    first_digit = None
    # initialize a variable to hold the last digit
    last_digit = None
    # loop through each character in the line
    for char in line:
        # if the character is a digit
        if char.isdigit():
            # if the first digit has not been set
            if first_digit is None:
                # set the first digit
                first_digit = char
            # if the first digit has been set
            else:
                # set the last digit
                last_digit = char
    # combine the first digit and the last digit to form a single two-digit number
    if last_digit is None:
        last_digit = first_digit
    number = int(first_digit + last_digit)
    # add the two-digit number to the list of numbers
    numbers.append(number)

# sum the list of numbers
total = sum(numbers)
print(total)