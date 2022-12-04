#This is the code for AOC day 4--->contains both the parts
file1 = open("day4.txt","r")
data = file1.read().split('\n') #reading the file
count = count2 =0
for i in range(len(data)):
    word = data[i]
    range1 = (word.split(','))[0]
    range2 = (word.split(','))[1]
    lower1 = int((range1.split('-')[0]))
    upper1 = int((range1.split('-')[1]))
    lower2 = int((range2.split('-')[0]))
    upper2 = int((range2.split('-')[1])) 
    set1 = set()
    set2 = set()
    while(lower1<=upper1):
        set1.add(lower1)
        lower1+=1
    while(lower2<=upper2):
        set2.add(lower2)
        lower2+=1
    set3 = set1&set2
    if(set3 == set1 or set3 == set2):count+=1
    if(len(set3)!=0):count2+=1
print(count) #soln for the first problem
print(count2) #soln for the second problem