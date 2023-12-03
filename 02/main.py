import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def first_solution():
    result = 0

    with open("input.txt") as input_file:
        for line in input_file:
            
            gameId = re.match("Game (\d+):", line)[1]
            red_cubes = re.findall("(\d+) red", line)
            green_cubes = re.findall("(\d+) green", line)
            blue_cubes = re.findall("(\d+) blue", line)

            if (
                int(max([int(x) for x in red_cubes])) <= RED_MAX
                and int(max([int(x) for x in green_cubes])) <= GREEN_MAX
                and int(max([int(x) for x in blue_cubes])) <= BLUE_MAX
            ):
                result += int(gameId)
    
    print(result)

def second_solution():
    result = 0

    with open("input.txt") as input_file:
        for line in input_file:
            red_cubes = re.findall("(\d+) red", line)
            green_cubes = re.findall("(\d+) green", line)
            blue_cubes = re.findall("(\d+) blue", line)

            power = (
                int(max([int(x) for x in red_cubes]))
                * int(max([int(x) for x in green_cubes]))
                * int(max([int(x) for x in blue_cubes]))
            )

            result += power
    
    print(result)

second_solution()