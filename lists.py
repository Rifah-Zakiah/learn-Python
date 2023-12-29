#list = complex datatype which is a collection of primitive datatypes(int, float, char, str, bool)
marks = [95, 98, 97, 'math']
print(marks)
#To access indivual data: add index: index starts from 0; 
print(marks[0])
#negative index is possible, starts from last:
print(marks[1])
print(marks[-1])
print(marks[-4])
#To print a cluster of list:
print(marks[0:2])#prints 0 and 1 index elements;  
print(marks[1:3])
for score in marks:#This for loop prints all the item  of the list
    print(score)
#append:To add new element at the end of the list:
marks.append(99)
print(marks)
#insert: To add new element at the middle, i.e, at any index of the list; by mentioning the index before the element:
marks.insert(2, 88)#The marks 88 is added at the second index of the list.
print(marks)
#To find if any element exist in the list: output in true/false; by using the keyword 'in'-
print(99 in marks)
print(87 in marks)
#To print the length of the list by using 'len()':
print(len(marks))
#Printing the elements of the list by while loop:
i = 0
while i < len(marks):
    print(marks[i])
    i += 1
#Clear: To clear elements of the list:
marks.clear()
print(marks)