import numpy as np
file1 = open("day8.txt","r")
data = file1.read().split('\n')
row = len(data) #gives us the number of rows in the 2d matrix
col = len(data[0]) #gives us the number of cols in the 2d matrix
#defining the original and the new_matrix (one without borders)
arr = np.zeros((row,col),dtype=int)
new_arr = np.zeros((row-2,col-2),dtype = int)
total_count = 0 #will store the number of trees that can be visible from the outer grid
def total_trees_count(ele,lst): #This function gives the total trees count
    c = 0
    for k in lst:
        if(k>=ele):
            c+=1
            break
        else:
            c+=1
    return c
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
count = 0
lst_total_trees =[]
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
        ele = new_arr[i][j]
        up_count = total_trees_count(ele,(np.flip(col1[0:i+1])))
        down_count = total_trees_count(ele,col1[i+2:])
        left_count = total_trees_count(ele,(np.flip(row1[0:j+1])))
        right_count = total_trees_count(ele,(row1[j+2:]))
        lst_total_trees.append(up_count*down_count*left_count*right_count)
print(max(lst_total_trees))
        