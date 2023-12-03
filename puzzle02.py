import os

MAX_CUBES_Q1 = {"red": 12, "green": 13, "blue": 14}


def puzzler(file_name):
    sum1 = 0
    sum2 = 0
    with open(file_name) as file:
        for raw_line in file.readlines():
            game_dict = {}
            power = 1
            line = raw_line.strip()
            split_colon = line.split(":")
            for cube_set in split_colon[1].strip().split(";"):
                for cubes in cube_set.strip().split(","):
                    [number_str, color] = cubes.strip().split(" ")
                    number = int(number_str)
                    if color not in game_dict.keys():
                        game_dict[color] = number
                    elif game_dict[color] < number:
                        game_dict[color] = number
            possible = True
            for color in list(game_dict.keys()):
                if color in MAX_CUBES_Q1.keys():
                    power *= game_dict[color]
                    if game_dict[color] > MAX_CUBES_Q1[color]:
                        possible = False
            if possible:
                sum1 += int(split_colon[0].strip().split()[1])
            sum2 += power
    print(f"The answer to q1 using {file_name} is : {sum1}")
    print(f"The answer to q2 using {file_name} is : {sum2}")
    print("---")


puzzler("example02-1.txt")
puzzler("input02.txt")
