#CODE FOR DAY1
import numpy as np
file1 = open("day1.txt","r")
data = file1.read().split('\n')
data = data +['']
sum_list = []
ele_list = []
count = 0
for i in range(len(data)):
    if(data[i]!=''):
        ele_list.append(int(data[i]))
    else:
        sum_list.append(sum(ele_list))
        ele_list = []
sum_list = np.sort(sum_list)
total = sum_list[-1]+sum_list[-2]+sum_list[-3]
print(total)





