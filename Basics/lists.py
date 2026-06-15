# Lists in Python are ordered collections of items. They are mutable, meaning you can change their content without changing their identity. Lists are defined using square brackets []. 

# Example of list creation
my_list = [1, 2, 3, 4, 5]
print(my_list)
# Lists can contain items of different types
mixed_list = [1, "Hello", 3.14, True]

print(len(mixed_list)) # prints the length of the list, which is 4

print(mixed_list.index("Hello")) # prints the index of the first occurrence of "Hello" in the list, which is 1
# Methods for lists
# Lists have many built-in methods that allow you to manipulate and work with them. Here are some commonly used list methods:
# 1. append() - Adds an item to the end of the list
my_list.append(6)
print(my_list)
# 2. insert() - Inserts an item at a specified index
my_list.insert(0, 0) # inserts 0 at index 0
print(my_list)
# 3. remove() - Removes the first occurrence of a specified item
my_list.remove(3) # removes the first occurrence of 3 from the list
print(my_list)
# 4. pop() - Removes and returns the item at a specified index (default is the last item)
last_item = my_list.pop() # removes and returns the last item from the list
print(last_item)
print(my_list)
# 5. index() - Returns the index of the first occurrence of a specified item
index_of_2 = my_list.index(2) # returns the index of the first occurrence of 2 in the list
print(index_of_2)
# 6. count() - Returns the number of occurrences of a specified item in the list
count_of_2 = my_list.count(2) # returns the number of occurrences of 2 in the list
print(count_of_2)
# 7. sort() - Sorts the items of the list in ascending order
my_list.sort()
print(my_list)
# 8. reverse() - Reverses the order of the items in the list
my_list.reverse()
print(my_list)
# Indexing and slicing lists
# Lists in Python are indexed, which means you can access individual items using their index. The index starts from 0 for the first item, 1 for the second item, and so on. You can also use negative indexing to access items from the end of the list, where -1 is the last item, -2 is the second last item, and so on.
my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # prints 1
print(my_list[0:3]) # prints [1, 2, 3]