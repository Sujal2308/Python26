# Strings in Python
# Strings are sequences of characters enclosed in quotes. In Python, you can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """) to create strings.

# Example of string creation
str1 = 'Hello, World!'
str2 = "Python is great!"
str3 = '''This is a multi-line string.'''
print(str1)
print(str2)
print(str3)

# Methods for strings
# Strings have many built-in methods that allow you to manipulate and work with them. Here are some commonly used string methods:

# 1. len() - Returns the length of the string
print(len(str1))

# 2. lower() - Converts the string to lowercase
print(str1.lower())

# 3. upper() - Converts the string to uppercase
print(str1.upper())

# 4. strip() - Removes leading and trailing whitespace
str4 = "   Hello, World!   "
print(str4.strip())

print(str4.rstrip()) # removes trailing whitespace
print(str4.lstrip()) # removes leading whitespace

# 5. replace() - Replaces a specified substring with another substring
print(str1.replace("World", "Python"))

# 6. split() - Splits the string into a list of substrings based on a specified delimiter
print(str1.split(", ")) # splits the string into a list of two elements: ['Hello', 'World!']

# 7. join() - Joins a list of strings into a single string with a specified delimiter

newStr = "Hello World"
print(newStr.find("or")) # returns the index of the first occurrence of "or" in the string, which is 7 
print(newStr.find("o", 5)) # returns the index of the first occurrence of "o" in the string starting from index 5, which is 7

newStr.isalnum() # returns True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, otherwise returns False
newStr.isalpha() # returns True if all characters in the string are alphabetic (letters) and there is at least one character, otherwise returns False
newStr.isdigit() # returns True if all characters in the string are digits and there is at least one character, otherwise returns False
newStr.islower() # returns True if all characters in the string are lowercase and there is at least one character, otherwise returns False
newStr.isupper() # returns True if all characters in the string are uppercase and there is at least one character, otherwise returns False
newStr.isspace() # returns True if all characters in the string are whitespace and there is at least one character, otherwise returns False                 


#Indexing and slicing strings
# Strings in Python are indexed, which means you can access individual characters using their index. The index starts from 0 for the first character, 1 for the second character, and so on. You can also use negative indexing to access characters from the end of the string, where -1 is the last character, -2 is the second last character, and so on.    

my_string = "Hello, World!"
print(my_string[0]) # prints 'H'

print(my_string[0:7]) # prints 'Hello, ' (slices the string from index 0 to index 6)
print(my_string[7:]) # prints 'World!' (slices the string from index 7 to the end of the string)
print(my_string[:5]) # prints 'Hello' (slices the string from the beginning to index 4)
print(my_string[-6:]) # prints 'World!' (slices the string from index -6 to the end of the string)  


#Strings are immutable in Python, which means you cannot change the characters in a string after it has been created. However, you can create a new string by concatenating or slicing existing strings.    
str5 = str1 + " " + str2 # concatenates str1 and str2 with a space in between
print(str5)

#! ord() - returns the Unicode code point of a given character
print(ord('A')) # prints 65