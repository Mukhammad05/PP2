# # task 1
def squares_generator(N):
    for i in range(1, N+1):
        yield i*i

N = int(input("Enter number: "))
for square in squares_generator(N):
    print(square)

# task 2
def Even_Number(N):
    for i in range(0, N+1):
        if i % 2 == 0:
            yield i

N = int(input("Enter number: "))
squares = Even_Number(N)
squares_list = list(squares)
print(','.join(map(str,squares_list)))

# task 3
def Divided(N):
    for i in range(0, N+1):
        if i % 4 == 0 and i % 3 == 0:
            yield i
        

N = int(input("Enter number: "))
variables = Divided(N)
squares_list = list(variables)
print(','.join(map(str,squares_list)))

# task 4
def squares(A, B):
    for i in range(A, B+1):
        yield i**2

A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
number = squares(A, B)
squares_solution = list(number)
print(','.join(map(str,squares_solution)))

# task 5
def Return(N):
    while N >= 0:
        yield N
        N -= 1

N = int(input("Enter N: "))
Return_f = Return(N)
Return_List = list(Return_f)
print(','.join(map(str,Return_List)))



