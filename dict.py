#Dictionary: To store values in pairs;
marks = {'eng' : 88, 'phy' : 98, 'chem' : 97, 'bio' : 96}
#The strings can be passed as keys instead of index to print that certain element:
print(marks['bio'])
#To add new elements in the dictionary,
marks['math'] = 99
print(marks)
#In order to change existing element value,
marks['eng'] = 91
print(marks) 