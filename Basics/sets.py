# sets are the unordered collection of unique elements. They are mutable, meaning you can add or remove elements from a set after its creation. Sets are defined using curly braces {} or the set() constructor.

# Example of set creation
my_set = {1, 2, 3, 4, 5}
print(my_set)

myset2 = set([1, 2, 3, 4, 5])
print(myset2)

# empty set
empty_set = set()
print(type(empty_set))

# methods for sets
# 1. add() - Adds an element to the set
my_set.add(6)
print(my_set)

# 2. remove() - Removes a specified element from the set. Raises a KeyError if the element is not found.
my_set.remove(3)
print(my_set)

# 3. discard() - Removes a specified element from the set. Does not raise an error if the element is not found.
my_set.discard(10) # does not raise an error

# 4. pop() - Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
removed_element = my_set.pop()
print(f"Removed element: {removed_element}")

# 5. clear() - Removes all elements from the set
my_set.clear()

print(my_set)

