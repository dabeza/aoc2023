import elf


def puzzler(file_name):
    data = elf.get_data(file_name)
    sum1 = 0
    copies = [1] * len(data)
    card_index = 0
    for line in data:
        split_line = line.split("|")
        winners = set()
        contenders = set()
        for number in split_line[0].split(":")[1].split():
            winners.add(int(number))
        for number in split_line[1].split():
            contenders.add(int(number))

        matches = winners.intersection(contenders)

        if matches:
            points = 2 ** (len(matches) - 1)
            added_copies = copies[card_index]
            for i in range(card_index + 1, card_index + len(matches) + 1):
                copies[i] += added_copies

        else:
            points = 0
        sum1 += points

        card_index += 1

    print(f"The answer to q1 using {file_name} is : {sum1}")
    print(f"The answer to q2 using {file_name} is : {sum(copies)}")
    print("")


puzzler("example04-1.txt")
puzzler("input04.txt")
