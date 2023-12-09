import pytest
from part2 import find_text_digits
def test_find_text_digits():
    # Test case 1: Text digits present in the line
    line = "1dhfone4ah8thahk"
    expected_output = [(4, '1')]
    assert find_text_digits(line) == expected_output

    # Test case 2: No text digits present in the line
    line = "abcdefghijklmnopqrstuvwxyz1"
    expected_output = []
    assert find_text_digits(line) == expected_output

    # Test case 3: Text digits present multiple times in the line
    line = "abcdeonefghijksevenlmnopqrstufivevwxyz1"
    expected_output = [(5, '1'), (14, '7'), (29, '5')]
    assert find_text_digits(line) == expected_output

    # Test case 4: Text digits sharing letters
    line = "7eighthreeight6"
    expected_output = [(1, '8'), (5, '3'), (9,'8')]
    assert find_text_digits(line) == expected_output


test_find_text_digits()