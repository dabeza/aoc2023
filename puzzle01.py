import os

NMBRS = "123456789"
NMBR_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def puzzler(file_name):
    sum1 = 0
    sum2 = 0
    with open(file_name) as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            # Puzzle 1
            index_first = 9999
            index_last = -1
            first = None
            last = None
            for nmbr in NMBRS:
                index = line.find(nmbr)
                if index < index_first and index > -1:
                    index_first = index
                    first = nmbr
                index = line.rfind(nmbr)
                if index > index_last:
                    index_last = index
                    last = nmbr
            if last and first :
                sum1 += int(first + last)
            
            if first:
                sub_first = line[:index_first]
                sub_last = line[index_last+1:]
            else:
                sub_first = line
                sub_last = line
                
            index_first = 9999
            index_last = -1
            for nmbr in list(NMBR_DICT.keys()):
                index = sub_first.find(nmbr)
                if index < index_first and index > -1:
                    first = NMBR_DICT[nmbr]
                    index_first = index
                index = sub_last.rfind(nmbr)
                if index > index_last:
                    index_last = index
                    last =  NMBR_DICT[nmbr]
            if first and last:
                sum2 += int(first + last)

            
            
    print(f"The answer to q1 using {file_name} is : {sum1}")
    print(f"The answer to q2 using {file_name} is : {sum2}")
    print("---")


puzzler("example01-1.txt")
puzzler("example01-2.txt")
puzzler("input01.txt")
