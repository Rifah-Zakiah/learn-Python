#Set: unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values. {} is used.
#Elements of a set is immutable; however elements can be added or removed from a set.
#Unordered values = no Index in the elements of the set unlike touple or list.
marks = {99, 97, 98, 97}
print(marks)#97 will be printed only once
#Since no index, we need to run a loop to print all the elements of the set:
for score in marks:
    print(score)  