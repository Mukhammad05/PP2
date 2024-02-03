# task 1
print("Hello")
print('Hello')

# task 2
a = "Hello"
print(a)

# task 3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# task 4
a = "Hello, World!"
print(a[1])

# task 5
for y in 'KBTU':
    print(y)

# task 6
a = "Hello, My friend!"
print(len(a))

# task 7
txt = "The best things in life are free!"
print("life" in txt)

# task 8
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
else:
    print("No")

# task 9
txt = "The best things in life are free!"
print("expensive" not in txt)

# task 10
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# task 11
b = "Hello, World!"
print(b[2:5])

# task 12
b = "Hello, KBTU!"
print(b[:5])

# task 13
b = "Hello, my country!"
print(b[2:])

# task 14
b = "Hello, city!"
print(b[-5:-2])

# task 15
a = "Hello, Ali!"
print(a.upper())

# task 16
a = "Hello, Student!"
print(a.lower())

# task 17 
a = " Hello, World! "
print(a.strip())

# task 18
a = "Hello, World!"
print(a.replace("H", "J"))

# task 19
a = "Hello, World!"
print(a.split(","))

# task 20
a = "Arman "
b = "Maqsat"
c = a + b
print(c)

# task 21
a = "My"
b = "friends"
c = a + " " + b
print(c)

# task 22
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# task 23
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# task 24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

# task 25
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

# task 26
x = "Hello World"
print(len(x))

# task 27
txt = "Hello World"
x = txt[0]

# task 28
txt = "Hello World"
x = txt[2:5]

# task 29
txt = " Hello World "
x = txt.strip()

# task 30
txt = "Hello World"
txt = txt.upper()

# task 31
txt = "Hello World"
txt = txt.lower()

# task 32
txt = "Hello World"
txt = txt.replace("H","J")

# task 33
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))