# task 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# task 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# task 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# task 4
fruits = ["apple", "banana", "cherry"]
print(fruits[2])

# task 5
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi" 

# task 6
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# task 7
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon") 

# task 8
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# task 9
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# task 10
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# task 11
fruits = ["apple", "banana", "cherry"]
print(len(fruits))