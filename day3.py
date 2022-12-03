#This is code for day3part1 AOC
file1 = open("day3.txt","r")
data = file1.read().split('\n')
common_list = []
for i in range(len(data)):
    word = data[i]
    word1 = word[0:len(word)//2]
    word2 = word[len(word)//2:len(word)]
    common_letter_list = list(set(word1)&set(word2))
    for j in common_letter_list:
        if(j.isupper()==True):
            common_list.append(ord(j)-38)
        else:
            common_list.append(ord(j)-96)
print(sum(common_list))