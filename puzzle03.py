import elf
import sys
        
        

def puzzler(file_name):
    data = elf.get_data(file_name)
    sum1 = 0
    file = open("output03.txt","w")
    for i in range(len(data)):
        cur=data[i].strip()
        if i >0:
            prv=data[i-1].strip()
        else :
            prv = "." * len(cur)    
        
        if i < len(data)-1:
            nxt = data[i+1].strip()
        else:
            nxt = "." * len(cur)
        j = 0
        while j < len(cur):
            number =""
            start = None
            while j<len(cur) and cur[j].isdigit():
                if start is None:
                    start = j -1
                if start < 0:
                    start = 0

                number +=cur[j]
                j += 1
            if number:
                stop = j + 1
                if stop > len(cur):
                    stop = j
                print(number,file=file)
                perimiter = ""
                perimiter += prv[start:stop]
                if start > 0:
                    perimiter += cur[start]
                if stop <len(cur):
                    perimiter += cur[stop-1]
                perimiter += nxt[start:stop]
                print(perimiter,file=file)
                print("",file=file)
                for char in perimiter:
                    if char != "." and not char.isdigit():
                        sum1 += int(number)
                        break
            j+=1
            
                


    print(f"The answer to q1 using {file_name} is : {sum1}")
            


puzzler("example03-1.txt")
puzzler("input03.txt")