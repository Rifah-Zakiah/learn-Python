age = int(input("Enter your age:"))
#In python, blocks of code is differentiiated by indentations(tab space) unlike {} which is used in other languages
if age >= int(18):
    print("You are an adult")
    print("You can vote")
    #This two codes are the part of same ifin this indentation.
elif age<int(18) and age>=int(4):
    print("You are in school")
else: 
    print("You are in school")
#BUILDING A MINI CALC THROUGH PYTHON:
n1 = int(input("Enter first number:"))
op = input("Enter the listed operators(+, -, *, /, %):")
n2 = int(input("Enter second number:"))
if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
elif op == '%':
    print(n1 % n2)
#Using the range keyword: range of numbers from 0 to 5 (0, 1, 2, 3, 4) where 5 is not included;
print(range(5))