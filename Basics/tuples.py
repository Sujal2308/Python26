# Tuples are similar to lists, but they are immutable, meaning that once a tuple is created, it cannot be modified. Tuples are defined using parentheses () instead of square brackets [].

# Example of tuple creation
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# Tuples can also contain items of different types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

# Methods for tuples
# Since tuples are immutable, they have fewer built-in methods compared to lists. Here are some commonly used tuple methods:
# 1. count() - Returns the number of occurrences of a specified item in the tuple
count_of_2 = my_tuple.count(2) # returns the number of occurrences of 2 in the tuple
print(count_of_2)

# 2. index() - Returns the index of the first occurrence of a specified item
index_of_2 = my_tuple.index(2) # returns the index of the first occurrence of 2 in the tuple
print(index_of_2)   


# Indexing and slicing tuples
# Like lists, tuples are also indexed, and you can access individual items using their index.
print(my_tuple[0]) # prints 1
print(my_tuple[0:3]) # prints (1, 2, 3)

# empty tuple
empty_tuple = ()
print(empty_tuple)



temp = (1)
print(type(temp)) # prints <class 'int'>, not a tuple

#! single element tuple (note the comma)
single_element_tuple = (1,)
print(single_element_tuple)