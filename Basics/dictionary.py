# Dictionaries are unordered collections of key-value pairs. They are defined using curly braces {} with keys and values separated by colons :.

# Example of dictionary creation
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

# Accessing values in a dictionary
print(my_dict["name"]) # prints Alice
print(my_dict.get("age")) # prints 30

# Adding and modifying items in a dictionary
my_dict["email"] = "alice@example.com" # adds a new key-value pair
my_dict["age"] = 31 # modifies the value of an existing key
print(my_dict)

# Removing items from a dictionary
del my_dict["city"] # removes the key-value pair with key "city"
print(my_dict)

# Dictionary methods
# 1. keys() - Returns a list of all keys in the dictionary
print(my_dict.keys())

# 2. values() - Returns a list of all values in the dictionary
print(my_dict.values())

# 3. items() - Returns a list of all key-value pairs in the dictionary
print(my_dict.items())

# 4. get() - Returns the value for a specified key, or a default value if the key is not found
print(my_dict.get("name")) # prints Alice
print(my_dict.get("height", "Not specified")) # prints Not specified

# 5. update() - Updates the dictionary with key-value pairs from another dictionary or iterable
my_dict.update({"height": 5.8, "weight": 150})
print(my_dict)
# 6. pop() - Removes and returns the value for a specified key
age = my_dict.pop("age") # removes the key "age" and returns its value
print(f"Removed age: {age}")    

# how to create methods in dictionary

def sum(a,b):
    return a+b  

dict = {
    "sum": sum
}

#Note : You can also use lambda functions to create methods in a dictionary not regular function but you can create them outside and give its reference. For example:
dict2 = {
    "sum": lambda a, b: a + b
}

print(dict["sum"](5, 10)) # prints 15

# nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

print(nested_dict["person1"]["name"])

# if we try to create duplicate keys in dict then the new value will be override with older one and no error occur

# note it is not compulsary to write keys in double quotes but its a good practice
temp_dict = {
    id : 101,
    age : 21,
    age : 22
}

print(temp_dict[id])