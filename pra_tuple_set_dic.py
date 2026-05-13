# x = {1,2,3}
# print(x)
# x.add(4)
# print(x)
# x.update([5,6,7])
# print(x)
# x.update({8,9,10})
# print(x)
# x.pop() # removes and returns an arbitrary element from the set
# print(x)
# x.remove(2)
# print(x)
# x.discard(5) # discard does not raise an error if the element is not found
# print(x)
# x.clear()
# print(x)
# x = {1, 2, 3}
# y = {3, 4, 5}
# print(x.union(y)) # {1, 2, 3, 4, 5}
# print(x.intersection(y)) # {3}
# print(x.difference(y)) # {1, 2}
# print(x.symmetric_difference(y)) # {1, 2, 4, 5}

# x= {1, 2, 3}
# y = {3, 4, 5}
# print(x | y) # {1, 2, 3, 4, 5}
# print(x & y) # {3}  
# print(x - y) # {1, 2}
# print(x ^ y) # {1, 2, 4, 5}

# x = {1, 2, 3}
# y = {3, 4, 5}
# print(x.issubset(y)) # False
# print(x.issuperset(y)) # False  
# print(x.isdisjoint(y)) # False  #check and b have no common elements
# x = {1, 2, 3}
# print(len(x)) # 3
# print(max(x)) # 3
# print(min(x)) # 1
# print(sum(x)) # 6


# list1 = [1, 2, 3]
# set1 = set(list1)
# print(set1) # {1, 2, 3}
# set2 = {4, 5, 6}
# list2 = list(set2)
# print(list2) # [4, 5, 6]

# x=  {1, 2, 3}
# y = x.copy()
# print(x) # {1, 2, 3}
# print(y) # {1, 2, 3}
# y.add(4)
# print(x) # {1, 2, 3}
# print(y) # {1, 2, 3, 4}

# x = {1, 2, 3}
# y = x
# print(x) # {1, 2, 3}
# print(y) # {1, 2, 3}
# y.add(4)
# print(x) # {1, 2, 3, 4}
# print(y) # {1, 2, 3, 4}


# x ={3,6,4,5}
# y= sorted(x)
# print(y) # [3, 4, 5]

###########Dictionary#############
# x = {'a': 1, 'b': 2, 'c': 3}
# print(x) # {'a': 1, 'b': 2, 'c': 3}
# print(x.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])
# print(x.keys()) # dict_keys(['a', 'b', 'c'])
# print(x.values()) # dict_values([1, 2, 3])
# x["d"] = 4
# x["a"] = 10
# print(x) # {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# x.update({'e': 5})
# print(x) # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# x.pop('b')
# print(x) # {'a': 10, 'c': 3, 'd': 4, 'e': 5}
# x.popitem() # removes and returns an arbitrary key-value pair from the dictionary   
# print(x) # {'a': 10, 'c': 3, 'd': 4}
# del x['c']
# print(x) # {'a': 10, 'd': 4}
# x.clear()
# print(x) # {}

# x = {'a': 1, 'b': 2, 'c': 3}
# print('a' in x) # True
# print('d' in x) # False
# print(x.get('a')) # 1
# print(x.get('d')) # None
# print(x.get('d', 'Not found')) # Not found


# print(x.setdefault('d', 4)) # 4
# print(x) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(x.setdefault('a', 10)) # 1
# print(x) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d = {"a": 10}
# x = d.setdefault("a", 100)
# print(x) # 10
# x = d.setdefault("b", 20)
# print(x) # 20
# print(d) # {'a': 10, 'b': 20}

# x= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(len(x)) # 5
# print(max(x)) # 'e'
# print(min(x)) # 'a'
# print(sum(x.values())) # 15
# print(max(x.values())) # 5
# print(min(x.values())) # 1
# print(sorted(x)) # ['a', 'b', 'c', 'd', 'e']
# print(sorted(x, reverse=True)) # ['e', 'd', 'c', 'b', 'a']
# print(sorted(x.values())) # [1, 2, 3, 4, 5]
# print(sorted(x.values(), reverse=True)) # [5, 4, 3, 2, 1]
# print(sorted(x.items())) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# print(sorted(x.items(), reverse=True)) # [('e', 5), ('d', 4), ('c', 3), ('b', 2), ('a', 1)]
# print(sorted(x.values())) # [1, 2, 3, 4, 5]
# print(sorted(x.values(), reverse=True)) # [5, 4, 3, 2, 1]
# print(sorted(x.keys())) # ['a', 'b', 'c', 'd', 'e']
# print(sorted(x.keys(), reverse=True)) # ['e', 'd', 'c', 'b', 'a']
# print(list(x.values()).count(2)) # 1
# print(list(x.keys())) # ['a', 'b', 'c', 'd', 'e']
# print(list(x.values())) # [1, 2, 3, 4, 5]
# print(list(x.items())) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)] 
# print(x.copy()) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(x) # {'a': 1, 'b': 2, 'c':3, 'd': 4, 'e': 5}


# d= {'a': 1, 'b': 2, 'c': 3}
# e = d.copy()
# print(d) # {'a': 1, 'b': 2, 'c': 3}
# print(e) # {'a': 1, 'b': 2, 'c': 3}
# e['d'] = 4
# print(d) # {'a': 1, 'b': 2, 'c': 3}
# print(e) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d = {'a': 1, 'b': 2, 'c': 3}
# e = d
# print(d) # {'a': 1, 'b': 2, 'c': 3}
# print(e) # {'a': 1, 'b': 2, 'c': 3}
# e['d'] = 4
# print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(e) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# set1 = {'a', 'b', 'c'}
# dict1 = dict.fromkeys(set1, 0)
# print(dict1) # {'a': 0, 'b': 0, 'c': 0}
# dict2 = dict.fromkeys(set1, 1)  
# print(dict2) # {'a': 1, 'b': 1, 'c': 1}
# dict3 = dict.fromkeys(set1)
# print(dict3) # {'a': None, 'b': None, 'c': None}    
# l1 = ['a', 'b', 'c']
# d1 = {ch: 0 for ch in l1}
# print(d1) # {'a': 0, 'b': 0, 'c': 0}
# l2 = ['a', 'b', 'c']
# d2 = {ch: 1 for ch in l2}       
# print(d2) # {'a': 1, 'b': 1, 'c': 1}




# d= {}
# for ch in "banana":
#     d[ch] = d.get(ch, 0) + 1
# print(d) # {'b': 1, 'a': 3, 'n': 2}

# d = {}
# for ch in "mississippi":
#     d[ch] = d.get(ch, 0) + 1    
# print(d) # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# d={ch: "banana".count(ch) for ch in set("banana")}
# print(d) # {'b': 1, 'a': 3, 'n': 2}

# d={ch: "banana".count(ch) for ch in "banana"}
# print(d) # {'b': 1, 'a': 3, 'n': 2}
# string = "hello world"
# frequency = {}
# for char in string:
#     frequency[char] = frequency.get(char, 0) + 1
# print(frequency) # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# students = ["Alice", "Bob", "Charlie"]
# grades = [85, 90, 95]
# student_grades = dict(zip(students, grades))
# print(student_grades) # {'Alice': 85, 'Bob': 90, 'Charlie': 95}


# #give more examples of dictionary in python
# # Example 1: Creating a dictionary to store information about a person
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }  
# print(person) # {'name': 'John', 'age': 30, 'city': 'New York'}

# # Example 2: Accessing values in a dictionary
# print(person["name"]) # John
# print(person["age"]) # 30
# print(person.get("city")) # New York
# # Example 3: Adding and updating key-value pairs in a dictionary
# person["email"] = "john@example.com"
# print(person) # {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}
# person["age"] = 31
# print(person) # {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}   
# # Example 4: Removing key-value pairs from a dictionary
# del person["city"]
# print(person) # {'name': 'John', 'age': 31, 'email': 'john@example.com'}
# person.pop("email")
# print(person) # {'name': 'John', 'age': 31} 
# person.popitem()
# print(person) # {'name': 'John'}


# Example 5: Iterating over a dictionary
# person = {"name": "John","age": 30,"city": "New York"}  
# for key in person:
#     print(key,"=", person[key]) 
# for key, value in person.items():
#     print(key,":", value)  

# # Example 6: Using dictionary comprehensions
# square= {x: x**2 for x in range(1,6)}
# print(square) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}    

# cube = {x: x**3 for x in range(1,6)}
# print(cube) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# # Example 7: Merging two dictionaries
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 20, 'c': 30, 'd': 40}
# d1.update(d2)

# print(d1) # {'a': 1, 'b': 20, 'c': 30, 'd': 40}
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 20, "c": 30}
# merged_dict = {**dict1, **dict2}
# print(merged_dict) # {'a': 1, 'b': 20, 'c': 30} 

# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# merged = dict(list(d1.items()) + list(d2.items()))
# print(merged)

# # Example 8: Using the fromkeys() method to create a dictionary with default values
# keys = ["a", "b", "c"]
# default_value = 0
# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict) # {'a': 0, 'b': 0, 'c': 0}

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# new_dict = dict(zip(keys, values))
# print(new_dict) # {'a': 1, 'b': 2, 'c': 3}

# # Example 9: Using the setdefault() method to set default values in a dictionary
# person = {"name": "John", "age": 30}    
# print(person.setdefault("city", "New York")) # New York
# print(person) # {'name': 'John', 'age': 30, 'city': 'New York'}
# print(person.setdefault("name", "Alice")) # John
# print(person) # {'name': 'John', 'age': 30, 'city': 'New York'}

# # Example 10: Using the get() method to access values in a dictionary with a default value
# person = {"name": "John", "age": 30}   
# print(person.get(("name"))) # John
# print(person.get("city", "Not found")) # Not found
# print(person.get("age", "Not found")) # 30

# # Example 11: Using the items() method to iterate over key-value pairs in a dictionary
# person = {"name": "John", "age": 30, "city": "New York"}
# for key, value in person.items():
#     print(key, ":", value)

# #Example 12: Using the keys() method to iterate over keys in a dictionary    
# person = {"name": "John", "age": 30, "city": "New York"}
# for key in person.keys():
#     print(key)
# #Example 13: Using the values() method to iterate over values in a dictionary
# person = {"name": "John", "age": 30, "city": "New York"}
# for value in person.values():
#     print(value)

# keys = ["a", "b", "c"]
# values = [1, 2]

# new_dict = dict(zip(keys,values))
# print(new_dict)

# d = {"a": 1, "b": 2, "c": 3}

# swapped = dict(zip(d.values(), d.keys()))
# print(swapped)

# names = ["John", "Sam", "Alex"]
# marks = [85, 40, 90]

# d = dict(zip(names, marks))

# for name, mark in d.items():
#     if mark > 50:
#         print(name, ":",mark)
# print()

# products = ["pen", "book", "eraser"]
# prices = [10, 50, 5]

# d = dict(zip(products, prices))

# for k in d:
#     d[k] = d[k] * 1.10

# print(d)


# s = "python"
# d = dict(zip(s, range(len(s))))
# print(d)

# keys = ["a", "b", "a"]
# values = [1, 2, 3]

# d = dict(zip(keys, values))
# print(d)
##############Tuple#########################
x = (1,2,3,6,4,5)
print(type(x))
print(len(x))
print(sum(x))
print(max(x))
print(min(x))
print(x.count(1))
print(x.index(3))
print(sorted(x))
print(all(x))
print(any(x))
