#This is day2 of AOC
file1 = open("day2.txt","r")
data = file1.read().split('\n')
total_score = 0
for i in range(len(data)):
    score = 0
    str = data[i]
    opp = str[0]
    you = str[2]
    #now writing the if condition
    if(opp =='A' and you =='X'):
        #this results in draw-- both rock
        score = 3 + 1
    if(opp=='B' and you =='Y'):
        #this results in draw -- both paper
        score = 3 + 2
    if(opp=='C' and you == 'Z'):
        #this results in draw-- both scissor
        score = 3 + 3
    #now checking for other conditions---first where the opponent wins
    if(opp=='A' and you =='Z'):
        #I have taken scissor
        score = 0 + 3
    if(opp=='C'and you =='Y'):
        #I have taken paper
        score = 0 + 2
    if(opp=='B'and you =='X'):
        #I have taken rock
        score = 0 + 1
    #now taking the conditions where I am winning
    if(opp=='A' and you =='Y'):
        # I have taken paper
        score = 6 + 2
    if(opp=='B' and you == 'Z'):
        #I have taken scissor
        score = 6 + 3
    if(opp=='C'and you == 'X'):
        #I have taken rock
        score = 6 + 1
    total_score+= score
print(total_score)

