# functions are the block of code which performs a specific task. It is a reusable piece of code that can be called multiple times in a program. Functions are defined using the def keyword followed by the function name and parentheses. The code block within every function starts with a colon (:) and is indented.

# Example of a function definition
def greet(name):
    print(f"Hello, {name}!")
# Calling the function
greet("Alice") # prints Hello, Alice!

# Functions can also return values using the return statement. The return statement is used to exit a function and go back to the place where it was called, optionally passing back an expression to the caller.

def add(a, b):
    return a + b

result = add(5, 10)
print(result) # prints 15

# lambda functions, also known as anonymous functions, are small, unnamed functions defined using the lambda keyword. They can take any number of arguments but can only have one expression. The expression is evaluated and returned when the lambda function is called.

#! Example of a lambda function
square = lambda x: x * x
print(square(5)) # prints 25    

# returning multiple values from a function
def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age    
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}") # prints Name: Alice, Age: 30

# default arguments in functions
def greet(name="World"):
    print(f"Hello, {name}!")    

greet() # prints Hello, World!
greet("Alice") # prints Hello, Alice!

# scope of variables in functions
# Variables defined inside a function are local to that function and cannot be accessed outside of it.
def my_function():
    local_variable = "I am local to this function"
    print(local_variable)   
my_function() # prints I am local to this function
# print(local_variable) # This will raise an error because local_variable is not defined outside the function   

# global variables can be accessed and modified inside a function using the global keyword.
global_variable = "I am a global variable"  
def modify_global_variable():
    global global_variable # This tells Python that we want to use the global variable instead of creating a new local variable
    global_variable = "I have been modified inside the function"    

# none is a special constant in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value or that a function does not return anything.
def do_nothing():
    pass # pass is a placeholder statement that does nothing, it is used when a statement is required syntactically but you don't want to execute any code  
result = do_nothing()
print(result) # prints None, because the function does not return anything