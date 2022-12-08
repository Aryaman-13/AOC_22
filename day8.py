import numpy as np
file1 = open("day8.txt","r")
data = file1.read().split('\n')
row = len(data) #gives us the number of rows in the 2d matrix
col = len(data[0]) #gives us the number of cols in the 2d matrix
#defining the original and the new_matrix (one without borders)
arr = np.zeros((row,col),dtype=int)
new_arr = np.zeros((row-2,col-2),dtype = int)
total_count = 0 #will store the number of trees that can be visible from the outer grid
#initialising the matrix with the data
lst=[]
for i in range(len(data)):
    x = data[i]
    for j in range(len(x)):
        arr[i][j] = int(x[j])
#counting the number of border elements
for i in range(len(data)):
    for j in range(len(data[0])):
        if(i==0 or j==0 or i==row-1 or j==col-1):
            total_count+=1
        else:
            lst.append(arr[i][j])
print(total_count)
count = 0
for i in range(len(new_arr)):
    for j in range(len(new_arr[0])):
        new_arr[i][j]=lst[count]
        count+=1
#now we will be checking for the non-boundary elements
for i in range(len(new_arr)):
    left = []
    right = []
    up = []
    down = []
    for j in range(len(new_arr[0])):
        row1 = arr[i+1,:]
        col1 = arr[:,j+1]
        # print(row1)
        left = row1[0:j+1]
        right = row1[j+2:]
        up = col1[0:i+1]
        down = col1[i+2:]
        ele = new_arr[i][j]
        lst1=[]
        lst1.append(max(left))
        lst1.append(max(right))
        lst1.append(max(up))
        lst1.append(max(down))
        lst1.append(ele)
        print(lst1)
        if(ele>max(up) or ele> max(down) or ele>max(right) or ele>max(left)):
            total_count+=1
print(total_count)

        

