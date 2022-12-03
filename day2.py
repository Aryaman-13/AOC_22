#This is day2 of AOC
file1 = open("day2.txt","r")
data = file1.read().split('\n')
total_score = 0
for i in range(len(data)):
    score = 0
    str = data[i]
    opp = str[0]
    you = str[2]
    #writing the dfferent conditions
    if(opp=='A'):
        if(you=='X'): #draw
            score = 3+1
        elif(you=='Z'): #lose
            score = 0 + 3
        else: #win
            score = 6 + 2
    if(opp=='B'):
        if(you=='Y'):#draw
            score = 3 + 2
        elif(you=='X'):#lose
            score = 0 + 1
        else: #win
            score = 6 + 3
    if(opp=='C'):
        if(you=='Z'):#draw
            score = 3 + 3
        elif(you=='Y'):#lose
            score = 0 + 2
        else: #win
            score = 6 + 1
    total_score+= score
print(total_score)