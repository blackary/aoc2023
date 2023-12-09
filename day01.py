import re
from pathlib import Path

input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

input = Path("input01").read_text()

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def get_matches(input: str, items_to_match: list[str]) -> list[str]:
    """Given an input string, and a list of potential items to match,
    return a list of all matches found, IN ORDER in the input string, INCLUDING if any
    overlap with each other.

    Uses regex, so the items to match can be regex patterns.
    """

    pattern = "|".join(map(re.escape, items_to_match))

    matches = re.findall(f"(?=({pattern}))", input)

    return matches


assert get_matches("one2three", ["one", "two", "three"]) == ["one", "three"]

# Test one where there is an overlap between two matches

assert get_matches("twone", ["one", "two", "three"]) == ["two", "one"]


s = 0
for row in input.splitlines():
    nums_found = get_matches(row, list(nums.keys()))
    print(row, nums_found)
    digits_found = [nums[n] for n in nums_found]
    # nums = re.findall(r"\d", row)
    first, last = digits_found[0], digits_found[-1]

    s += int(first + last)

print(s)
