def safeLine(input):
    safeness = False
    line = input.split()
    line = [int(i) for i in line]
    if line == sorted(line) or line == sorted(line, reverse=True):
        for l in range (len(line)):
            if l != len(line)-1:
                if abs(line[l]-line[l+1]) > 0 and abs(line[l]-line[l+1]) <= 3:
                    safeness = True
                else:
                    safeness = False
                    break
            else:
                break            
    else:
        safeness = False
    return safeness


def isSafe(input):
    counter = 0
    with open(file=input,mode="r") as file:
        lines = file.readlines()
        for l in lines:
            safe = safeLine(l)
            if safe:
                counter += 1
            else:
                continue
    return counter


def dampener(input):
    line = input.split()
    safeness = False
    if safeLine(" ".join(line)) == True:
        safeness = True
    else:
        dampenerCount = 0
        for i in range (len(line)): 
            withoutOne = line.copy()
            del withoutOne[i]
            if safeLine(" ".join(withoutOne)):
                dampenerCount += 1
        if dampenerCount >= 1:
            safeness = True
        else:
            safeness = False
    return safeness

def isSafeDampener(input):
    counter = 0
    with open(file=input,mode="r") as file:
        lines = file.readlines()
        for l in lines:
            safe = dampener(l)
            if safe:
                counter += 1
            else:
                continue
    return counter

         
        
file_path = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day2/inputDay2.txt"
file_path2 = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day2/exampleDay2.txt"
#print(isSafe(file_path))
#print(isSafe(file_path2))

print(isSafeDampener(file_path))
print(isSafeDampener(file_path2))

#print(safeLine("1 3 6 9 10 11"))
