#This is day3part2 AOC code
file1 = open("day3.txt","r")
data = file1.read().split('\n')
j = 0
common_list = []
while(j<len(data)):
    word1 = data[j]
    word2 = data[j+1]
    word3 = data[j+2]
    a = list(set(word1)&set(word2)&set(word3))
    for b in a:
        if(b.isupper()==True):
            common_list.append(ord(b)-38)
        else:
            common_list.append(ord(b)-96)
    j = j+3
print(sum(common_list))