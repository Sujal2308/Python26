# loops are the block of code that is repeated until a certain condition is met. There are two types of loops in python: for loops and while loops.

#! for loops are used to iterate over a sequence (like a list, tuple, string) or other iterable objects. The syntax of a for loop is:

#* range(a,b,c) determines start and end point of iteration where b is exclusive so loops run from a to b-1 and c is the step value which is optional and default is 1. If c is negative then it will decrement the value of i in each iteration.

#! note : a is optional if not give 0 is taken default but b(where to stop) is mandatory
# for i in range(0,10):
#     print(i)

#! if we have to decrement the value of i then we can use range(a,b,-1) where -1 is step value which is optional and default is 1
# for i in range(10,0,-1):
#     print(i)    

list = ["sujal","anil",10]

#loop run from 0 to len
# for i in range(len(list)):
#     print(list[i])

# another way without specifying end like for each
for i in list :
    print(i)

#! while loop

# k = 0;
# while(k<len(list)):
#     print(list[k])
#     k = k + 1

# multiplication table

def mul(num) :
    # for i in range(1,11):
    #     print(f"{num} * {i} = {num*i}")

    i =1
    while(i<=10):
         print(f"{num} * {i} = {num*i}")
         i = i+1;

mul(10)



def table(a):
    i = 1
    for j in range(i,11):
        print(a*j)

user_input = int(input("Enter value"))
table(user_input)