def filePrep(input):

    #Open document
    with open(input) as f:

    #create List    
        templineList = f.readlines()
        lineList = []
        for i in templineList:
            lineList.append(i.strip())
    # end of create List

    sum = 0

    
    for line in range (len(lineList)):
        
        # check for horizontals
        if "XMAS" in lineList[line]:
            sum += lineList[line].count("XMAS")
        if "SAMX" in lineList[line]:
            sum += lineList[line].count("SAMX")
        for character in range (len(lineList[line])):
            # look for every x
            if lineList[line][character]== 'X':
                # chek for verticals
                if line + 3 < len(lineList): 
                    if lineList[line+1][character] == 'M' and lineList[line+2][character] == 'A' and lineList[line+3][character] == 'S':
                        sum += 1
                if line - 3 >= 0:
                    if lineList[line-1][character] == 'M' and lineList[line-2][character] == 'A' and lineList[line-3][character] == 'S':
                        sum += 1
                
                # check for diagonals
                #rechts unten
                if line + 3 < len(lineList) and character + 3 < len(lineList[line]): 
                    if lineList[line+1][character+1] == 'M' and lineList[line+2][character+2] == 'A' and lineList[line+3][character+3] == 'S':
                        sum += 1
                #links oben
                if line - 3 >= 0 and character + 3 < len(lineList[line]):
                    if lineList[line-1][character+1] == 'M' and lineList[line-2][character+2] == 'A' and lineList[line-3][character+3] == 'S':
                        sum += 1
                #rechts oben
                if line + 3 < len(lineList) and character - 3 >= 0: 
                    if lineList[line+1][character-1] == 'M' and lineList[line+2][character-2] == 'A' and lineList[line+3][character-3] == 'S':
                        sum += 1
                #rechts unten
                if line - 3 >= 0 and character - 3 >= 0:
                    if lineList[line-1][character-1] == 'M' and lineList[line-2][character-2] == 'A' and lineList[line-3][character-3] == 'S':
                        sum += 1
    return sum

#X S
#M A
#A M
#S X


#part 2

def xMas(input):
    with open(input, "r") as file:
        counter = 0
        templineList = file.readlines()
        text = []
        for i in templineList:
            text.append(i.strip())
        print(text)
        
        for line in range (1,len(text)-1):
            for charakter in range(1,len(text[line])-1):
                #print("line: ", line, "column: ", charakter, "Value: ",text[line][charakter])
                if text[line][charakter] == 'A':
                    #print("line: ", line, "column: ", charakter, "Value: ",text[line][charakter], "A detected")
                    if (text[line+1][charakter+1] == 'S' and text[line-1][charakter-1] == 'M'):
                        if (text[line-1][charakter+1] == 'S' and text[line+1][charakter-1] == 'M') or (text[line-1][charakter+1] == 'M' and text[line+1][charakter-1] == 'S'):
                            counter += 1
                        
                    elif (text[line+1][charakter+1] == 'M' and text[line-1][charakter-1] == 'S'):
                        if (text[line-1][charakter+1] == 'S' and text[line+1][charakter-1] == 'M') or (text[line-1][charakter+1] == 'M' and text[line+1][charakter-1] == 'S'):
                            counter += 1
                    else:
                        continue
        
        return counter
                 
                        

file_path = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day4/inputDay4.txt"
file_path2 = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day4/exampleDay4.txt"

print(xMas(file_path))
print(xMas(file_path2))