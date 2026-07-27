# break, continue and pass are the three keywords in python that are used to control the flow of loops.

#! break is used to exit the loop when a certain condition is met. It is used to terminate the loop and exit from it.

#! continue is used to skip the current iteration of the loop and move to the next iteration. It is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.

#! pass is used as a placeholder for future code. It is used when you want to write a loop or a function but you don't want to write the code inside it yet. It is used to avoid syntax errors when you have an empty block of code.

for i in range(5):
    print(i)
    if(i==3):
        break # 0 1 2 3 terminates

for i in range(5):
    if(i==2):
        continue
    print(i) #0,1,3,4 (2 is skipped)
 

for i  in range(5):
    pass