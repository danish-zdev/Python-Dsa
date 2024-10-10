# Methods

# all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
# any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# len()	Return the length (the number of items) in the dictionary.
# sorted()	Return a new sorted list of keys in the dictionary.
# clear()	Removes all items from the dictionary.
# keys()	Returns a new object of the dictionary's keys.
# values()	Returns a new object of the dictionary's values



# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary




test_dict1 = {'silver': 4, 'gold': 2, 'diamond': 5}
print("The original dictionary ", test_dict1)
test_dict2 = {}
# print(reversed(test_dict1))
for key in reversed(test_dict1):
    test_dict2[key] = test_dict1[key]
    print("The reversed order dictionary ", test_dict2)


d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
d_swap = {v: k for k, v in d.items()}
print(d_swap)
#   or 

# inv_map = {}
# for k, v in d.items():
#     inv_map[v] = inv_map.get(v, []) + [k]

# print(inv_map)    



x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
# z = x|y
# z = {**x, **y}
z= dict(x.items() | y.items())
print(z)
