#this is day2 part2
file1 = open("day2.txt","r")
data = file1.read().split('\n')
total_score = 0
for i in range(len(data)):
    score = 0
    str = data[i]
    opp = str[0]
    outcome = str[2]
    if(outcome=='Y'): #case when I need to draw
        if(opp=='A'):
            #I also need to choose rock
            score = 3 + 1
        if(opp=='B'):
            #I need to choose paper
            score = 3 + 2
        if(opp=='C'):
            #I need to choose scissor
            score = 3 + 3
    if(outcome =='X'): # case when I need to lose
        if(opp=='A'):
            # I need to choose scissor
            score = 0+ 3
        if(opp=='B'):
            # I need to choose rock
            score = 0 + 1
        if(opp=='C'):
            #I need to choose paper
            score = 0 + 2
    if(outcome == 'Z'): #case where I am winning
        if(opp=='A'):
            # I need to choose paper
            score = 6 + 2
        if(opp=='B'):
            #I need to choose scissor
            score = 6+3
        if(opp=='C'):
            #I need to choose rock
            score = 6+1
    total_score+=score
print(total_score)
