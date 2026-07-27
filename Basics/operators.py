# Operators are the symbols that perform specific operations on one, two, or more operands and return a result.

# Arithmetic Operators  include addition (+), subtraction (-), multiplication (*), division (/), modulus (%), exponentiation (**), and floor division (//).
a = 14
b = 5
c = a + b  # Addition
print("Addition:", c)
c = a - b  # Subtraction
print("Subtraction:", c)
c = a * b  # Multiplication
print("Multiplication:", c)
c = a / b  # Division
print("Division:", c)
c = a % b  # Modulus
print("Modulus:", c)
c = a ** b  # Exponentiation (a raised to the power of b)
print("Exponentiation:", c)
c = a // b  # Floor Division (returns the truncated integer value of the division example: 14 // 5 = 2)
print("Floor Division:", c)


# Comparison Operators include equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).

# Logical Operators include and, or, and not. These operators are used to combine conditional statements.

# Assignment Operators include =, +=, -=, *=, /=, %=, **=, and //=. These operators are used to assign values to variables.

# Bitwise Operators include &, |, ^, ~, <<, and >>. These operators are used to perform bit-level operations on binary numbers.


#! Membership Operators include in and not in. These operators are used to test whether a value is present in a sequence (like a list, tuple, or string).
#Example: 
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 not in my_list)  # Output: True

#! Identity Operators include is and is not. These operators are used to compare the memory locations of two objects.
a = 10
b = 10
c = 20
print(a is b)  # Output: True
print(a is c)  # Output: False
print(a is not c)  # Output: True

#  Ternary Operator (Conditional Expression) is a one-liner replacement for the if-else statement. It is used to evaluate a condition and return one of two values based on whether the condition is True or False.

x = 10 
y = 20 
z = x if x > y else y  # Ternary Operator
print("Ternary Operator:", z)

