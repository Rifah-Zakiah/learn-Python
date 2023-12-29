print("Hi")#normal printing statement
print("I have made it??")
print('Yeahoo')
name = "Rifah"#String type variable
age = 10299 #Integer type variable but dtores as string
#if later in the code the variable is changed then the value stored also changes
name = "Rif"
age = 55
print(name)
print(age)
#Taking input:
Name = input("What is your name? ")
print("Hello " + Name) # + is used to concatenate the two strings
sh_name = input("What is your superhero name? ")
print("Are you really " + sh_name + "?")
#Type conversion: 
n = 18
print(float(18)) # int is an integer which is converted to float
#To print summation of two numbers:
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
c = n1 + n2
print("The contenated result is " + c)
sum = int(n1) + int(n2) #Type conversion is very crucial for python as all are initially considered as string.
print("The sum of the two numbers is: " + str(sum))#But concatenation only occurs in string; so the int sum needs to be converted to string

