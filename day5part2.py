#This is day5 code for AOC
file1 = open("day5.txt","r")
data = file1.read().split('\n') #reading the file
# print(data)

#creating stack before any movement of the transposition
stack1 = []
stack1.append('R')
stack1.append('N')
stack1.append('F')
stack1.append('V')
stack1.append('L')
stack1.append('J')
stack1.append('S')
stack1.append('M')

stack2 = []
stack2.append('P')
stack2.append('N')
stack2.append('D')
stack2.append('Z')
stack2.append('F')
stack2.append('J')
stack2.append('W')
stack2.append('H')

stack3 = []
stack3.append('W')
stack3.append('R')
stack3.append('C')
stack3.append('D')
stack3.append('G')

stack4 = []
stack4.append('N')
stack4.append('B')
stack4.append('S')

stack5 = []
stack5.append('M')
stack5.append('Z')
stack5.append('W')
stack5.append('P')
stack5.append('C')
stack5.append('B')
stack5.append('F')
stack5.append('N')

stack6 = []
stack6.append('P')
stack6.append('R')
stack6.append('M')
stack6.append('W')

stack7 = []
stack7.append('R')
stack7.append('T')
stack7.append('N')
stack7.append('G')
stack7.append('L')
stack7.append('S')
stack7.append('W')

stack8 = []
stack8.append('Q')
stack8.append('T')
stack8.append('H')
stack8.append('F')
stack8.append('N')
stack8.append('B')
stack8.append('V')

stack9 = []
stack9.append('L')
stack9.append('M')
stack9.append('H')
stack9.append('Z')
stack9.append('N')
stack9.append('F')
#done with all the initiailising

for i in range(len(data)):
    str = data[i]
    letter_list = str.split(" ")
    num_cargo = int(letter_list[1])
    ini_stack = int(letter_list[3])
    final_stack = int(letter_list[5])
    j = 1
    temp_stack = []
    while(j<=num_cargo):
        #popping the crate from the initial stack
        if(ini_stack==1):ele = stack1.pop()
        if(ini_stack==2):ele = stack2.pop()
        if(ini_stack==3):ele = stack3.pop()
        if(ini_stack==4):ele = stack4.pop()
        if(ini_stack==5):ele = stack5.pop()
        if(ini_stack==6):ele = stack6.pop()
        if(ini_stack==7):ele = stack7.pop()
        if(ini_stack==8):ele = stack8.pop()
        if(ini_stack==9):ele = stack9.pop()
        #pushing the crate to the final stack
        temp_stack.append(ele)
        j = j+1
        
    while(len(temp_stack)!=0):
        ele2 = temp_stack[-1]
        if(final_stack==1):stack1.append(ele2)
        if(final_stack==2):stack2.append(ele2)
        if(final_stack==3):stack3.append(ele2)
        if(final_stack==4):stack4.append(ele2)
        if(final_stack==5):stack5.append(ele2)
        if(final_stack==6):stack6.append(ele2)
        if(final_stack==7):stack7.append(ele2)
        if(final_stack==8):stack8.append(ele2)
        if(final_stack==9):stack9.append(ele2)
        temp_stack.pop()
print(stack1[-1],stack2[-1],stack3[-1],stack4[-1])
print(stack5[-1],stack6[-1],stack7[-1],stack8[-1],stack9[-1])
