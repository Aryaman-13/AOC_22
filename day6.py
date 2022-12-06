#This is code for day6 AOC
file1 = open("day6.txt","r")
data = file1.read().split('\n')
str = data[0]
x = a = 0
for i in range(4,len(str)):
    sub_word = str[a:i]
    l1 = sub_word[0]
    l2 = sub_word[1]
    l3 = sub_word[2]
    l4 = sub_word[3]
    if(sub_word.count(l1)==1 and sub_word.count(l2)==1 and sub_word.count(l3)==1 and sub_word.count(l4)==1):
        print(i)
        break
    a+=1