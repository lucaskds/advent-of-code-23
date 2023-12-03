import re

result = 0
MAPPED_NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
}

def get_first_number(line: str, reversed: bool=False) -> int:
    if reversed:
        digit = re.search("(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d){1}", line[::-1])[0]
    else:
        digit = re.search("(one|two|three|four|five|six|seven|eight|nine|\d){1}", line)[0]

    return digit if digit.isnumeric() else MAPPED_NUMBERS[digit]

with open("input.txt") as input_file:
    for line in input_file:
        result += int(get_first_number(line) + get_first_number(line, True))

print(result)
