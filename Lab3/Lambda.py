# task 1
x = lambda a: a + 10
print(x(5))

# task 2
x = lambda a, b: a * b
print(x(5, 6))

# task 3
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# task 4
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# task 5
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# task 6
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))

# task 7
x = lambda a:a
