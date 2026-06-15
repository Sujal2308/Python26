# User Input
# #input() function is used to take input from user and it always returns string. So we need to type cast it to the required data type.
# wrap the input function with the type you want to convert it to, for example int() for integers, float() for floating point numbers, etc.

op = input("Enter the operation: ")
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
if(op=="+"):
    print("Sum is: ",num1+num2)
elif (op=="-"):
    print("Sub is: ",num1-num2)
else:
    print("Enter valid op")