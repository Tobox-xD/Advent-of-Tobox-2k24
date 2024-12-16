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

file_path = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day4/inputDay4.txt"
file_path2 = "C:/Users/Tobia/OneDrive/Dokumente/AdventOfCode24/Day4/exampleDay4.txt"

print(filePrep(file_path))
print(filePrep(file_path2))