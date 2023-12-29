#tuple: a type of list which cannot be further modified; initialised by ().
#Immutable: cannot change/mutate, remove or add an element of a tuple once declared.
marks = (99, 97, 98, 95, 97, 97)
#Counting numbers of repeated elements in tuple:
print(marks.count(97))
print(marks.count(98))
print(marks.count(90))
#Print the index of the element:
print(marks.index(98))
#() is optional in tuple; without any parenthesis it'll be by default considered as a tuple:
name ='rina', 'tina', 'hina', 'lina'
print(name)