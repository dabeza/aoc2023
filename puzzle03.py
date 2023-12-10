import elf
import sys


def check_perimiter_char(char, star_dict, row, col, number):
    if char != ".":
        if char == "*":
            star_coord = (row, col)
            add_star_dict(star_dict, star_coord, number)
        return True
    return False


def add_star_dict(star_dict: dict, star_coord, number):
    if star_coord in star_dict.keys():
        star_dict[star_coord].append(int(number))
    else:
        star_dict[star_coord] = [int(number)]


def puzzler(file_name):
    data = elf.get_data(file_name)
    sum1 = 0
    file = open("output03.txt", "w")
    columns = len(data[0].strip())
    star_dict = {}
    for row in range(len(data)):
        cur = data[row].strip()
        if row > 0:
            prv = data[row - 1].strip()
        else:
            prv = "." * columns

        if row < len(data) - 1:
            nxt = data[row + 1].strip()
        else:
            nxt = "." * columns
        col = 0
        while col < columns:
            number = ""
            start = None
            while col < columns and cur[col].isdigit():
                if start is None:
                    start = col - 1
                if start < 0:
                    start = 0

                number += cur[col]
                col += 1
            if number:
                stop = col + 1
                if stop > columns:
                    stop = col
                is_part_number = False

                # top
                sub_string = prv[start:stop]
                for sub_string_column in range(len(sub_string)):
                    char = sub_string[sub_string_column]
                    is_part_number |= check_perimiter_char(
                        char, star_dict, row - 1, sub_string_column + start, number
                    )

                # left
                if start > 0:
                    char = cur[start]
                    is_part_number |= check_perimiter_char(
                        char, star_dict, row, start, number
                    )

                # right
                if stop < columns:
                    char = cur[stop - 1]
                    is_part_number |= check_perimiter_char(
                        char, star_dict, row, stop - 1, number
                    )

                # bottom
                sub_string = nxt[start:stop]
                for sub_string_column in range(len(sub_string)):
                    char = sub_string[sub_string_column]
                    is_part_number |= check_perimiter_char(
                        char, star_dict, row + 1, sub_string_column + start, number
                    )

                if is_part_number:
                    sum1 += int(number)
            col += 1

    sum2 = 0
    print(star_dict, file=file)
    for numbers in list(star_dict.values()):
        if len(numbers) == 2:
            # print(numbers)
            gear_ratio = numbers[0] * numbers[1]
            sum2 += gear_ratio

    print(f"The answer to q1 using {file_name} is : {sum1}")
    print(f"The answer to q2 using {file_name} is : {sum2}")
    print("")


puzzler("example03-1.txt")
puzzler("input03.txt")
