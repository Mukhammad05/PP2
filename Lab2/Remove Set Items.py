# task 1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# task 2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# task 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal

# task 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# task 5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists
