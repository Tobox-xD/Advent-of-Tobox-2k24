import re

def mulExtractorFile(input):
    with open(input, "r") as f:
        text = f.read()
        #Struktur: mul(a,b)
        x = re.findall(r"mul\((\d+),(\d+)\)",text)
        print(x)
        mulSum = 0
        for i in x:
            mulSum += int(i[0])*int(i[1])
    return mulSum

def mulExtractor(input):
    x = re.findall(r"mul\((\d+),(\d+)\)",input)
    #print(x)
    mulSum = 0
    for i in x:
        mulSum += int(i[0])*int(i[1])
    return mulSum


def disabler(input):
    x = re.finditer(r"don't\(()\)",input)
    return(x)

def enabler(input):
    x = re.finditer(r"do\(()\)",input)
    return(x)


def mulDecider(text):

    mulSum = 0
    startpos = 0
    endpos = len(text)

    disabledList = disabler(text)
    disableStarts = []
    enabledList = enabler(text) 
    enableStarts = []

    for i in disabledList:
        disableStarts.append((i.start(),"d"))
    for i in enabledList:
        enableStarts.append((i.start(), "e"))

    sequence = disableStarts + enableStarts
    sequence.sort(key=lambda x: x[0])
    sequence.append((len(text),"end"))
    print(sequence)

    enabled = True

    for s in range (len(sequence)):
        match sequence[s][1]:
            case "d":
                if enabled:
                    endpos = sequence[s][0]
                else:
                    continue

            case "e":
                if not enabled:
                    startpos = sequence[s][0]
                    enabled = True
                    continue
                else:
                    continue 
                
            case "end":
                if enabled:
                    endpos = sequence[s][0]
                else:
                    continue

            case _:
                print("asd")
                
        mulSum += mulExtractor(text[startpos:endpos])
        enabled = False
    
    return  mulSum 

         
def starter(input):
    with open(input,"r") as f:
        text = f.read()
        return mulDecider(text)


file_path = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day3/inputDay3.txt"
file_path2 = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day3/exampleDay3.txt"
file_path3 = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day3/exampleDay3_2.txt"

print(starter(file_path))
print(starter(file_path3))


