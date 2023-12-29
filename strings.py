#discusses about various string operations
name = "Tony Stark"
print(name.upper())#Returns a string with all uppercase
print(name.lower())#Returns a string with all lowercase
print(name)#The above to string operation does not change the original string.
#To find a character or substring in a string:
print(name.find('S'))#Returns the index of the character if present otherwise a negative value(-1)
print(name.find('h')) 
print(name.find("ny"))#returns the index of the first character of the substring
#To replace a portion of the string:
print(name.replace("Tony Stark", "Ironman"))
print(name.replace('T', 'R'))
print(name)#The above to string operation does not change the original string.
#To check if a character or substring exists in a string: 'in' keyword (gives the result in true or false)
print('T' in name)
print('u' in name)
age = "20"
print(age.isdigit())#True
print(age.isalpha())#False
print(name*3)#prints the name 3 times
