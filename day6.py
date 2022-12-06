file1 = open("day6.txt","r")
data = file1.read().split('\n')
def get_index(data,y):
    a = 0
    str = data[0]
    for i in range(y,len(str)):
        sub_word = str[a:i]
        count = 0
        for j in sub_word:
            if(sub_word.count(j)>1):
                count+=1
        if(count==0):
            return i
            break
        a+=1
print(get_index(data,4)) #soln for the first question
print(get_index(data,14)) #soln for the second question



