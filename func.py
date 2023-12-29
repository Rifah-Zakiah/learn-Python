#Function: in-built, module, user defined
#Module function: related function and related variable stored in a single file; has to be imported.
import math #math is file containing arious math related functions
print(dir(math)) #'dir()' is used to print all the functions included in the file 'math'
#A function of 'math' is 'sqrt'. In order to use that,
from math import sqrt #This line imports 'sqrt' function from 'math'
print(sqrt(16)) 
#To import all the functions from 'math':
from math import *
print(sqrt(4))
#User defined functions:
def sum(n1, n2 = 4): #Values can be assigned in parameters so that if any value is not passed the default value is printed;
    print(n1 + n2)

sum(1, 2)
sum(1)#Here by default the value of n2 will be 4 since its value is not passed.