# task 1
l = [1,2,3,4,5]
print("result:", eval('*'.join(str(item) for item in l)))

# task 2

x = input("Enter string: ")

upper_case_number = 0
lower_case_number = 0

for i in x:
    if i.isupper():
        upper_case_number += 1
    elif i.lower():
        lower_case_number += 1

print(upper_case_number)
print(lower_case_number)

# task 3
stroka = str(input("Enter the string:"))
reversed_stroka = ''.join(reversed(stroka))
if reversed_stroka == stroka:
    print("String is a palindrome")
else:
    print("String isn't palindrome")

# task 4
    
import time
import math

def calculate_square_root(number):
    return math.sqrt(number)

input_number = int(input("Enter the number: "))
delay_ms = int(input("Enter the delay time in milliseconds: "))

time.sleep(delay_ms / 1000)  
result = calculate_square_root(input_number)

print(f"The square root of number {input_number} after {delay_ms} milliseconds is {result}")


# task 5
def all_true_tuple(tuple):
    return all(tuple)

tuple_1 = (True, True, False, True)
print(all_true_tuple(tuple_1))  
tuple_2 = (True, True, True, True)
print(all_true_tuple(tuple_2))











# # task 1
# from functools import reduce

# def multiply_list(numbers):
#     result = reduce(lambda x, y: x * y, numbers)
#     return result

# numbers = [2, 3, 4, 5]
# result = multiply_list(numbers)
# print("Multiplication result:", result)


# # task 2

# x = input("Enter string: ")

# upper_case_number = 0
# lower_case_number = 0

# for i in x:
#     if i.isupper():
#         upper_case_number += 1
#     elif i.lower():
#         lower_case_number += 1

# print(upper_case_number)
# print(lower_case_number)

# # task 3
# string = input("Enter a string: ")

# string = ''.join(char.lower() for char in string if char.isalnum())

# if string == string[::-1]:
#     print("Yes, it's a palindrome!")
# else:
#     print("No, it's not a palindrome.")

# # task 4
# import time
# import math

# number = int(input("Enter the number: "))
# milliseconds = int(input("Enter the milliseconds delay: "))

# time.sleep(milliseconds / 1000)

# result = math.sqrt(number)

# print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

# # task 5
# tuple1 = (True, True, True)
# tuple2 = (True, False, True)

# result1 = all(tuple1)
# print(result1)  

# result2 = all(tuple2)
# print(result2)  


    